# Step 2
Now, we are going extend the functionality from having to run the program for each prompt to being able to just run the program once and have a chat loop (amnesic) with the model.

We are also now using the `/api/chat` endpoint instead of the `/api/generate` enpoint. This is because the next step, which is adding state, is made easier by using the `/api/chat` endpoint that Ollama provides instead of creating our own logic for doing this, though we could certainly do that if we would like.

> [!note]
> The `raw` and `thinking` body parameters we were passing are no longer available as the `/api/chat` endpoint has a bit of a different shape. That is okay though as our previous steps already illustrated that without a chat template prompt (provided by `raw` set to false) and without a thinking prompt/training the LLM is kind of "dumb", especially a smaller model like the `qwen3.5:9b` that I am using. While these are important aspects of extending a model into an agent, we don't have to get caught up in them as most providers already supply that behavior/functionality out of the box, but this is quite interesting and worth taking a deeper look at at a different time.

## Amnesic Chat Loop
This chat loop is amnesic. For now...

This illustrates a core principle about LLMs, the models themselves are stateless!

Here are two examples of what you might see from this amnesic version:
```
# EXAMPLE 1
# ---------
you> Hello, my name is bob!
bot> Hello Bob! It's nice to meet you. How can I help you today?

you> What is my name?
bot> I actually don't know your name! If you'd like to share it with me, feel free to do so—I'll remember it for our conversation.

# EXAMPLE 2
# ---------
you> I like eggs.
bot> That's great! Eggs are such a versatile and delicious food. 🍳

Do you have a favorite way to cook them? I'm all for scrambled, fried (with those crispy edges), hard-boiled, or even baked into an omelet!

you> What do I like?
bot> I don't have access to your personal preferences or history unless you share them with me! 😊 To help figure out what *you* might like, could you tell me a bit about:
- Hobbies or activities you enjoy?
- Foods you love (or avoid)?
- Books, movies, music, or other media you gravitate toward?
- Values or goals that matter to you?

The more you share, the better I can tailor suggestions! What would you like to explore? 🌟
```
