from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# -----------------------------------------
# Conversation history
# -----------------------------------------

conversation = []


# -----------------------------------------
# Generate response
# -----------------------------------------

def generate_response(user_text):

    # Add user's message to history
    conversation.append(f"User: {user_text}")

    # Create complete conversation
    prompt = """
You are a helpful chatbot.

Conversation:
""" + "\n".join(conversation) + """

Assistant:
"""

    # Tokenize
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Generate
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False
    )

    # Convert tokens to text
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Add assistant response to history
    conversation.append(f"Assistant: {response}")

    return response



print("Transformer Chatbot")
print("Type 'exit' to stop.\n")


while True:

    user_text = input("You: ")

    if user_text.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = generate_response(user_text)

    print("Bot:", response)
    print()