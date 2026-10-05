# Step 3
Now we can extend our amnesic chat loop from Step 2 into a chat loop with memory.

## Memory
Instead of passing a single message each time, the user's latest message, we now pass all of the messages (both user's and model's) so they all populate the context and are taken into account, thus allowing the model/agent to "remember" things!

You might notice that each turn the full history is re-sent and re-processed which causes long conversations to become slower and more costly. This is why context management is so imporatnt and becomes a real problem for agents later.

```
you> Hello! My name is Billy.
bot> Hello Billy! It's nice to meet you. How can I help you today?
-----------------------------------
|  Context now holds 2 messages.  |
-----------------------------------

you> Could you reming me what my name is?
bot> Of course! You're Billy! It was nice to meet you earlier.
-----------------------------------
|  Context now holds 4 messages.  |
-----------------------------------

you> Wow, you have great memory!
bot> That's very kind of you to say! Thank you. I try my best to pay attention to everything we talk about in this chat so I can be as helpful as possible.

Is there anything else on your mind today that you'd like to chat about or need help with?
-----------------------------------
|  Context now holds 6 messages.  |
-----------------------------------
```
