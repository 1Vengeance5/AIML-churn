# Task 2 - Level 1

from transformers import pipeline

assistant = pipeline("text-generation", model="gpt2")

print("Campus Assistant (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    prompt = f"Question about a university campus: {user_input}\nAnswer:"
    response = assistant(prompt, max_length=80, num_return_sequences=1)

    print("Assistant:", response[0]["generated_text"])
