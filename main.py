import streamlit as st
from pathlib import Path
import openvino_genai as ov_genai
from llm_config import convert_and_compress_model
import time

# Predefined settings
MODEL_ID = "gemma-2-9b-it"
COMPRESSION_VARIANT = "INT4"
DEVICE = "CPU"
USE_PRECONVERTED = True

MODEL_CONFIGURATION = {
    "model_id": "google/gemma-2-9b-it",
    "remote_code": False,
    "start_message": (
        "Ah, you’ve summoned me, mighty one! I am your friendly, magical assistant, ready to grant you "
        "three wishes… er, well, actually, more than three answers! I’ll give you helpful, respectful, "
        "and honest answers, all wrapped up in a mystical cloud of wisdom. Fear not, for I shall keep my answers "
        "safe and positive, avoiding any dark magic, negativity, or harm. Ask away, and I’ll share knowledge fit for royalty!"
    ),
    "history_template": (
        "<start_of_turn>user{user}<end_of_turn><start_of_turn>model{assistant}<end_of_turn>"
    ),
    "current_message_template": (
        "<start_of_turn>user{user}<end_of_turn><start_of_turn>model{assistant}"
    ),
    "rag_prompt_template": (
        "You are a genie assistant, here to grant wishes in the form of knowledge! Use the following pieces of "
        "retrieved context to answer the question. If you don’t know the answer, just say that even a genie can’t "
        "know it all. Be concise and keep the magic alive, just like a good wish, keep it sweet and to the point. "
        "<start_of_turn>user{input}<end_of_turn><start_of_turn>context{context} <end_of_turn><start_of_turn>model"
    ),
}

# Load and prepare the model
@st.cache_resource
def load_model():
    try:
        model_dir = convert_and_compress_model(
            MODEL_ID,
            MODEL_CONFIGURATION,
            COMPRESSION_VARIANT,
            USE_PRECONVERTED,
        )
        pipe = ov_genai.LLMPipeline(str(model_dir), DEVICE)
        return pipe
    except Exception as e:
        st.error(f"Error during model setup: {e}")
        return None

# App Configuration
st.set_page_config(
    page_title="Aladdin",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)
logo_path = "E:\\ai pc\\logo.jpg" 

st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
        }
        .header h1 {
            font-size: 2.5rem;
            margin: 0;
        }
        .tagline {
            text-align: center;
            font-family: 'Arial', sans-serif;
            font-size: 1.2rem;
            color: white;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: white;
            margin-top: 50px;
        }
        .footer span {
            font-weight: bold;
            color: #007BFF;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_code = """
<style>
    @keyframes subtleGlow {
        0% { text-shadow: 0 0 5px #9b59b6, 0 0 5px #9b59b6; opacity: 0.7; }
        50% { text-shadow: 0 0 5px #8e44ad, 0 0 5px #8e44ad; opacity: 1; }
        100% { text-shadow: 0 0 5px #9b59b6, 0 0 5px #9b59b6; opacity: 0.7; }
    }

    .header h1 {
        font-size: 5rem;
        letter-spacing: 10px;
        color: #e5e4e2 ; /* Set the text color */
        animation: subtleGlow 4s infinite;
    }

    .tagline {
        font-size: 1.5rem;
        color: #d4af37;
        margin-top: 20px;
    }

    .header h1::before {
        content: "🧞‍♂️"; /* Use the genie emoji */
        font-size: 4rem;
        position: absolute;
        left: 80px;
        color: #ffffff; /* Original color for the emoji */
    }
</style>
<div class="header">
    <h1>Aladdin</h1>
</div>
<p class="tagline">I don’t grant three wishes, I grant unlimited wishes 🌠</p>
"""

st.markdown(html_code, unsafe_allow_html=True)



pipe = load_model()

if "input_prompt" not in st.session_state:
    st.session_state["input_prompt"] = ""

st.subheader("What will you ask the genie for?")

col1, col2 = st.columns(2)

suggested_questions = [
    "What are Aladdin’s powers?",
    "Who freed the genie?",
    "Who is Aladdin's rival?",
    "What was the genie's curse?",
]

selected_question = None

with col1:
    for i in range(0, len(suggested_questions), 2):  # Loop through odd indices
        if st.button(suggested_questions[i], key=f"suggest_{suggested_questions[i]}"):
            selected_question = suggested_questions[i]  # Update selected question

with col2:
    for i in range(1, len(suggested_questions), 2):  # Loop through even indices
        if st.button(suggested_questions[i], key=f"suggest_{suggested_questions[i]}"):
            selected_question = suggested_questions[i]  # Update selected question

if selected_question and not st.session_state["input_prompt"]:
    st.session_state["input_prompt"] = selected_question

input_prompt = st.text_area(
    "What do you wish for today?",
    value=st.session_state["input_prompt"],
    key="input_prompt",
    height=80,  # Adjust height to make it smaller
    max_chars=200  # Limit the input length
)

# Generate response button
st.markdown(
    """
    <style>
        .stButton button {
            background: linear-gradient(135deg, #6a11cb, #2575fc);  /* Purple to blue gradient */
            color: white;  /* White text */
            font-size: 1.2rem;  /* Increase font size */
            padding: 12px 24px;  /* Add padding */
            border-radius: 12px;  /* Rounded corners */
            border: none;  /* Remove border */
            transition: background 0.3s, transform 0.3s, box-shadow 0.3s;  /* Smooth transition */
        }

        .stButton button:hover {
            background: linear-gradient(135deg, #2575fc, #6a11cb);  /* Reverse gradient on hover */
            transform: scale(1.1);  /* Slightly enlarge the button on hover */
            box-shadow: 0 4px 8px rgba(37, 117, 252, 0.4);  /* Soft blue shadow */
        }

        .stButton button:active {
            transform: scale(1.05);  /* Slightly shrink the button on click */
            box-shadow: 0 4px 8px rgba(37, 117, 252, 0.6);  /* More prominent shadow on click */
        }

        .stButton button:focus {
            outline: none;  /* Remove the outline */
            box-shadow: 0 0 10px rgba(37, 117, 252, 0.7);  /* Blue glow on focus */
        }
    </style>
    """, 
    unsafe_allow_html=True
)
if "history" not in st.session_state:
    st.session_state["history"] = [] 

if st.button("Make a wish"):
    if input_prompt.strip():
        with st.spinner("Aladdin is granting your wish..."):
            try:
                time.sleep(1)                
                output = pipe.generate(input_prompt, max_new_tokens=200)
                st.success("Abracadabra – here comes your wish!")
                st.write(output)
                st.session_state["history"].append({"input": input_prompt, "output": output})
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a wish!")

# Display history
if st.checkbox("View wish history"):
    for i, entry in enumerate(st.session_state["history"]):
        st.write(f"**Wish {i + 1}:** {entry['input']}")
        st.write(f"**Response:** {entry['output']}")

# Footer with animation
st.markdown(
    """
    <style>
        @keyframes pulse {
            0% { opacity: 0.7; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.05); }
            100% { opacity: 0.7; transform: scale(1); }
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9rem;
            color: #555;
        }
        .footer span {
            animation: pulse 2s infinite;
            font-weight: bold;
            color: #007BFF;
        }
    </style>
    <div class="footer">
        Powered by <span>Gemma AI</span>. Built with ❤️ using OpenVINO & Streamlit.
    </div>
    """,
    unsafe_allow_html=True,
)
