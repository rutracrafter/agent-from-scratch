# Agent from Scratch
This is a repo I created for my own practice and learning that guides you through creating an agent from scratch!

> [!note]
> This is focused on agents, which are built on top of LLM models, rather than LLM models themselves.

## Setup
I am using Ollama to run a small local model (`qwen3.5:9b`), however this can be done with smaller or larger local models. You also don't need to use local models at all and can instead rely on api calls to services like OpenRouter or your preferred model provider.

## Structure
The idea is that each step in the process is self-contained in its own directory, and each step introduces something new. Step 0 can be thought of as the "testing setup" step where we just make a call to the llm provider. Step 1 is where things get interesting as we actually start creating an agent.

Each step directory has its own README.md which provides details, explanations, examples, etc.
