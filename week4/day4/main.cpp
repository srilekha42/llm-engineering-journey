#include <iostream>
#include <vector>
#include <numeric>
#include <thread>
#include <chrono>
#include <iomanip>
#include <algorithm> // For std::min

// Struct to hold a double value aligned to cache line size (typically 64 bytes).
// This helps prevent false sharing, a performance bottleneck where threads
// contend for the same cache line even if they're updating different variables.
struct AlignedDouble {
    double value;
    // Padding to ensure each AlignedDouble instance resides in its own cache line.
    // Common cache line sizes on AMD64 are 64 bytes.
    char padding[64 - sizeof(double)]; 
};

// Thread worker function to compute a partial sum of the Leibniz series.
// It utilizes an optimized form of the series: (1/(4j+1) - 1/(4j+3))
// This form reduces branch mispredictions and improves suitability for compiler-level vectorization,
// as each iteration processes two terms of the original series.
void thread_worker(long long start_j, long long end_j, AlignedDouble& local_aligned_sum) {
    double local_sum = 0.0;
    for (long long j = start_j; j < end_j; ++j) {
        local_sum += 1.0 / (4.0 * j + 1.0) - 1.0 / (4.0 * j + 3.0);
    }
    local_aligned_sum.value = local_sum;
}

int main() {
    // The original number of iterations from the Python code.
    const long long num_iterations_py = 200000000;

    // Determine the optimal number of threads to use based on hardware concurrency.
    // Fallback to 1 if hardware_concurrency() returns 0 or is not well-defined.
    long long num_threads = std::thread::hardware_concurrency();
    if (num_threads == 0) {
        num_threads = 1;
    }

    // The optimized series form processes two original terms per 'j' iteration.
    // Therefore, we effectively have num_iterations_py / 2 'j' iterations to process.
    long long total_j_iterations = num_iterations_py / 2;

    // Adjust num_threads if the total work is less than the available cores,
    // to avoid overhead from idle threads.
    if (total_j_iterations == 0) { // Special case for very small input (0 or 1 Python iterations)
        num_threads = 1;
    } else if (num_threads > total_j_iterations) {
        num_threads = total_j_iterations;
    }

    // Vectors to store thread-local sums and thread objects.
    // AlignedDouble is used for sums to prevent false sharing.
    std::vector<AlignedDouble> thread_sums(num_threads);
    std::vector<std::thread> threads;
    threads.reserve(num_threads); // Pre-allocate memory for thread objects

    // Record the start time for performance measurement.
    auto start_time = std::chrono::high_resolution_clock::now();

    // Distribute the 'j' iterations among the threads.
    // Each thread gets 'chunk_size' iterations, with the remainder distributed
    // by giving one extra iteration to the first 'remainder' threads.
    long long base_chunk_size_j = total_j_iterations / num_threads;
    long long remainder_j = total_j_iterations % num_threads;

    for (long long i = 0; i < num_threads; ++i) {
        // Calculate the starting 'j' index for the current thread.
        // It's the base cumulative sum of chunks plus any extra iterations from previous threads.
        long long thread_start_j = i * base_chunk_size_j + std::min(i, remainder_j);
        
        // Calculate the ending 'j' index for the current thread.
        // It's the starting index plus the base chunk size, plus one extra if this is one of the remainder threads.
        long long thread_end_j = thread_start_j + base_chunk_size_j + (i < remainder_j ? 1 : 0);
        
        // Ensure the last thread's end_j exactly matches the total_j_iterations to cover all work.
        if (i == num_threads - 1) {
            thread_end_j = total_j_iterations;
        }
        
        // Launch a new thread, passing its work range and a reference to its aligned sum.
        threads.emplace_back(thread_worker, thread_start_j, thread_end_j, std::ref(thread_sums[i]));
    }

    // Wait for all worker threads to complete their execution.
    for (auto& t : threads) {
        t.join();
    }

    // Aggregate the partial sums from all threads to get the final sum.
    double pi_approx_val = 0.0;
    for (const AlignedDouble& sum_obj : thread_sums) {
        pi_approx_val += sum_obj.value;
    }

    // Handle the final term if the original number of Python iterations was odd.
    // The grouped (1/(4j+1) - 1/(4j+3)) calculation covers original 'i' values from 0 up to 2*total_j_iterations - 1.
    // If num_iterations_py is odd, the very last term (for i = num_iterations_py - 1) is not covered.
    // This term is always positive: +1.0 / (2.0 * (num_iterations_py - 1) + 1.0),
    // which simplifies to +1.0 / (2.0 * num_iterations_py - 1.0).
    if (num_iterations_py % 2 == 1) {
        pi_approx_val += 1.0 / (2.0 * num_iterations_py - 1.0);
    }

    // Multiply the sum by 4.0 to obtain the final approximation of Pi.
    pi_approx_val *= 4.0;

    // Record the end time and calculate the elapsed duration.
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    // Output the results, matching the formatting style of the Python script.
    std::cout << std::fixed << std::setprecision(10) << "C++ Result  : " << pi_approx_val << std::endl;
    std::cout << std::fixed << std::setprecision(6) << "C++ Time    : " << elapsed.count() << " seconds" << std::endl;

    return 0;
}