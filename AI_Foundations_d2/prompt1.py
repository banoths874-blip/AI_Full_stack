
from ollama import chat

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : "summarize how the sky is red in colour in evening."
        }
    ]
)

print(response.message.content)