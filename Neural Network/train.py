import pandas as pd

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer
)


# ==========================================
# 1. Load dataset
# ==========================================

df = pd.read_csv("ai_ml_dataset_10000.csv")

print(df.head())
print("Total examples:", len(df))


# ==========================================
# 2. Convert pandas -> Hugging Face Dataset
# ==========================================

dataset = Dataset.from_pandas(df)


# ==========================================
# 3. Train/Test split
# ==========================================

dataset = dataset.train_test_split(
    test_size=0.2,
    seed=42
)

train_dataset = dataset["train"]
test_dataset = dataset["test"]


# ==========================================
# 4. Load FLAN-T5
# ==========================================

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# ==========================================
# 5. Tokenization
# ==========================================

def preprocess_function(examples):

    inputs = [
        "Answer the following AI/ML question: " + text
        for text in examples["input"]
    ]

    model_inputs = tokenizer(
        inputs,
        max_length=128,
        truncation=True
    )

    labels = tokenizer(
        text_target=examples["output"],
        max_length=128,
        truncation=True
    )

    model_inputs["labels"] = labels["input_ids"]

    return model_inputs


tokenized_train = train_dataset.map(
    preprocess_function,
    batched=True
)

tokenized_test = test_dataset.map(
    preprocess_function,
    batched=True
)


# ==========================================
# 6. Data collator
# ==========================================

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model
)


# ==========================================
# 7. Training configuration
# ==========================================

# training_args = Seq2SeqTrainingArguments(

#     output_dir="./flan_ai_ml",

#     eval_strategy="epoch",

#     learning_rate=2e-5,

#     per_device_train_batch_size=2,

#     per_device_eval_batch_size=2,

#     num_train_epochs=5,

#     weight_decay=0.01,

#     save_strategy="epoch",

#     logging_steps=10,

#     predict_with_generate=True,

#     report_to="none"
# )


training_args = Seq2SeqTrainingArguments(
    output_dir="./flan_ai_ml",
    eval_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    save_strategy="epoch",
    logging_steps=100,
    predict_with_generate=True,
    report_to="none"
)


# ==========================================
# 8. Trainer
# ==========================================

trainer = Seq2SeqTrainer(

    model=model,

    args=training_args,

    train_dataset=tokenized_train,

    eval_dataset=tokenized_test,

    processing_class=tokenizer,

    data_collator=data_collator
)


# ==========================================
# 9. TRAIN
# ==========================================

print("\nStarting training...\n")

trainer.train()


# ==========================================
# 10. Save trained model
# ==========================================

trainer.save_model("./my_ai_ml_model")

tokenizer.save_pretrained("./my_ai_ml_model")

print("\nTraining completed!")
print("Model saved in ./my_ai_ml_model")