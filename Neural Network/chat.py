from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# ==========================================
# Load YOUR fine-tuned model
# ==========================================

model_path = "./my_ai_ml_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)


# ==========================================
# Generate response
# ==========================================

def generate_response(question):

    prompt = "Answer the following AI/ML question: " + question

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        num_beams=4,
        do_sample=False
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer


# ==========================================
# Chat
# ==========================================

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = generate_response(question)

    print("Bot:", answer)