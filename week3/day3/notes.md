```python
# Week 3, Day 3: Tokenizers, Special Tokens, and Chat Templates

# 1. Words vs Numbers

# What is a Token?
# A token is a small piece of text.
# It can be a full word or part of a word.
# Example:
# "learning" -> "learn" + "ing"

# What is a Token ID?
# Every token gets a unique number.
# This number is called a Token ID.

# Main Rule:
# AI cannot understand text directly.
# It only understands numbers.
# The tokenizer changes text into numbers so the AI can understand it.


# 2. Every Model Has Its Own Tokenizer

# Each AI model has its own vocabulary (dictionary).
# The same Token ID can mean different things in different models.
# Example:
# Token ID 500 in Model A may be different from Token ID 500 in Model B.

# Always use the tokenizer made for your model.


# 3. What Are Special Tokens?

# Special tokens are extra markers that tell the AI about the message structure.

# Example:
# <|im_start|> -> Start of a message
# <|im_end|>   -> End of a message

# The AI understands these because it learned them during training.
# They are just special numbers for the model.


# 4. Chat Templates (apply_chat_template)

# We usually send messages like this:

messages = [
    {"role": "system", "content": "You are a helpful AI."},
    {"role": "user", "content": "Hello!"}
]

# apply_chat_template() changes this list into the correct format
# that the model expects before converting it into token IDs.

# In simple words:
# Human messages
#        ↓
# Chat Template
#        ↓
# Tokens
#        ↓
# Token IDs (Numbers)
#        ↓
# AI Model
```
