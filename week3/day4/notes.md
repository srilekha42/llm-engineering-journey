# Week 3, Day 4: Deep Model Architectures, Quantization, & Streaming Inference

## 1. Transformer Model Structure
A basic language model has three main parts:

- **Embedding Layer:** 
  Converts each word or token into a list of numbers (called a vector) that the computer can understand and process. These numbers capture the meaning of the word.

- **Decoder Layers (e.g., 24 Layers):** 
  These are the main processing layers. Each layer has two important parts:
  - **Self-Attention:** Looks at all the words in the input and finds which words are most related to each other. For example, in "She ate an apple," it understands that "ate" is related to "apple."
  - **MLP:** Takes the information from attention and adds more complexity. It helps the model learn deeper patterns by applying non-linear functions (like SiLU). This is like adding extra thinking power.

- **LM Head (Language Model Head):** 
  Takes the final processed information and predicts the probability of each possible next word. It decides which word is most likely to come next.

## 2. Quantization
- **What it is:** 
  Normally, model weights are stored as 16-bit floating-point numbers (FP16). Quantization converts them into 4-bit numbers (NF4), which are much smaller.
- **Why use it:** 
  This reduces GPU memory usage by up to 4 times. For example, a model that needs 4GB of memory can now run in just 1GB. The best part is that the model's quality and accuracy remain almost the same.

## 3. Streaming Inference
- **`model.generate()`:** 
  This is the function that runs the model step-by-step. It predicts one token at a time, and each new token is based on all the previous tokens. For example, it predicts the first word, then the second using the first, then the third using the first two, and so on.

- **`TextStreamer`:** 
  Normally, the model waits until it has generated the full response before showing it. TextStreamer changes that. It shows each word or token as soon as it is generated, so you can see the response building in real-time (like ChatGPT streaming).