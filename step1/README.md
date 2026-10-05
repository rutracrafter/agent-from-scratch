# Step 1
Now we take what we had in step 0 and build on it just a bit.

First, we add the `raw` parameter to the `generate()` function and `thinking` to the request's `options` body parameter. When true, this skips the chat template and thinking that ollama uses by default and causes the model to work at its most basic level which is continuing the text by generating the next token repeatedly.

Consequently, we also have to add the `options` parameter with `num_predict` set to a resonable number to the body of our request since if the raw parameter is specified and thinking is off, the LLM will most likely just keep on going on and on generating the next token which, without any guidance, tends to be tangentially related content.

For example if I send the prompt "2 + 2 = " and `raw` as true, the LLM will just keep generating text such as `4\n 3 + 3 = 9\n What is 5 * 3? The answer is 15...`. This is because it just keeps trying to generate the next probable Token. Try it yourself!

Notice how different the responses are when raw is true versus when it's false.
