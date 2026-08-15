#include <iostream>
#include <chrono>
#include <iomanip>

double calculate_pi(long long iterations = 200000000) {
    auto start_time = std::chrono::high_resolution_clock::now();

    double val = 0.0;
    double sign = 1.0; // Initial sign for i=0 term (1.0 / 1.0) is positive

    for (long long i = 0; i < iterations; ++i) {
        // Equivalent to: (-1.0 if i % 2 == 1 else 1.0) / (2.0 * i + 1.0)
        // By flipping 'sign' in each iteration, we avoid the modulo operation.
        val += sign / (2.0 * static_cast<double>(i) + 1.0);
        sign = -sign; // Flip sign for the next term
    }

    double pi_approx = val * 4.0;

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    std::cout << "C++ Result  : " << std::fixed << std::setprecision(10) << pi_approx << std::endl;
    std::cout << "C++ Time    : " << std::fixed << std::setprecision(6) << elapsed.count() << " seconds" << std::endl;

    return elapsed.count();
}

int main() {
    calculate_pi();
    return 0;
}