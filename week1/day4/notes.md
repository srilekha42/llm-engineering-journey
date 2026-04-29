# Day 4 — Core Concepts

## Tokens
- Token = piece of text (not always a word)
- Model works on tokens, not raw text
- More tokens = more cost

## Illusion of Memory
- LLM is stateless
- Chat memory = full conversation sent every time

## Context Window
- Max tokens model can handle
- Includes input + history + output

## API Cost
- Pay for input + output tokens
- Cost increases with conversation

## Scaling
- Training-time → bigger model
- Inference-time → better prompts

## Agents
- LLM + loop + tools