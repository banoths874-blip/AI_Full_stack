from ollama import chat
bad = "Tell me about cats"
good = "List 3 cat breeds that are suitable for a penthouse. 2 lines about each."

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : bad
        }
    ]
)

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : "summarize how the sky is red in colour in evening."
        }
    ]
)

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : good
        }
    ]
)

print(f"Bad Prompt Result:{responseB.message.content}")

print()

print(f"Good Prompt Result:{responseG.message.content}")