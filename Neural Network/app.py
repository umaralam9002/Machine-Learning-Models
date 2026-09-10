import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI/ML Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# TITLE
# =========================================================

st.title("🤖 AI/ML Chatbot")

st.caption(
    "Powered by your fine-tuned FLAN-T5 model"
)


# =========================================================
# AI/ML TOPICS
# =========================================================

AI_ML_TOPICS = [

    # Machine Learning
    "machine learning",

    # Supervised / Unsupervised Learning
    "supervised learning",
    "unsupervised learning",

    # Deep Learning
    "deep learning",

    # CNN
    "cnn",
    "convolutional neural network",
    "convolution neural network",
    "convolution",

    # RNN
    "rnn",
    "recurrent neural network",
    "recurrent neural networks",

    # LSTM
    "lstm",
    "long short term memory",
    "long short-term memory",

    # Transformer
    "transformer",
    "transformers",

    # NLP
    "nlp",
    "natural language processing",

    # Self Attention
    "self attention",
    "self-attention",
    "attention mechanism",

    # Embedding
    "embedding",
    "embeddings",
    "word embedding",
    "word embeddings",

    # ReLU
    "relu",
    "rectified linear unit",

    # Optimizer
    "optimizer",
    "optimizers",
    "optimization",
    "optimization algorithm",

    # Backpropagation
    "backpropagation",
    "back propagation",

    # Overfitting
    "overfitting"
]


# =========================================================
# CHECK AI/ML QUESTION
# =========================================================

def is_ai_ml_question(question):

    question = question.lower().strip()

    for topic in AI_ML_TOPICS:

        if topic in question:
            return True

    return False


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    model_path = "./my_ai_ml_model"

    tokenizer = AutoTokenizer.from_pretrained(
        model_path
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_path
    )

    return tokenizer, model


tokenizer, model = load_model()


# =========================================================
# GENERATE RESPONSE
# =========================================================

def generate_response(question):

    # -----------------------------------------------------
    # CHECK WHETHER QUESTION IS AI/ML RELATED
    # -----------------------------------------------------

    if not is_ai_ml_question(question):

        return (
            "I am trained on AI/ML data, so please ask me "
            "a relevant AI/ML question."
        )


    # -----------------------------------------------------
    # CREATE PROMPT
    # -----------------------------------------------------

    prompt = (
        "Answer the following AI/ML question clearly "
        "and accurately.\n\n"
        "Question: "
        + question
    )


    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )


    outputs = model.generate(
        **inputs,

        max_new_tokens=100,

        num_beams=4,

        do_sample=False
    )


    # -----------------------------------------------------
    # DECODE ANSWER
    # -----------------------------------------------------

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


    return answer


# =========================================================
# INITIALIZE CHAT HISTORY
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =========================================================
# DISPLAY PREVIOUS MESSAGES
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# CHAT INPUT
# =========================================================

user_question = st.chat_input(
    "Ask an AI/ML question..."
)


# =========================================================
# HANDLE USER QUESTION
# =========================================================

if user_question:

    # -----------------------------------------------------
    # DISPLAY USER MESSAGE
    # -----------------------------------------------------

    with st.chat_message("user"):

        st.markdown(
            user_question
        )


    # -----------------------------------------------------
    # SAVE USER MESSAGE
    # -----------------------------------------------------

    st.session_state.messages.append({

        "role": "user",

        "content": user_question

    })


    # -----------------------------------------------------
    # GENERATE ASSISTANT RESPONSE
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = generate_response(
                user_question
            )


        st.markdown(
            answer
        )


    # -----------------------------------------------------
    # SAVE ASSISTANT MESSAGE
    # -----------------------------------------------------

    st.session_state.messages.append({

        "role": "assistant",

        "content": answer

    })