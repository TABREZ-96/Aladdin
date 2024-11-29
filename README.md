# Aladdin

## Description

The **Aladdin Streamlit Application** is an interactive web-based AI assistant designed to simulate a genie that grants unlimited wishes in the form of knowledge and answers. It leverages **OpenVINO's GenAI** to handle queries using a pre-trained model. This app features a beautifully styled interface with dynamic animations, predefined prompts, and input customization.

---

## Features

- **AI-Powered Genie:** Powered by OpenVINO GenAI with compression for optimized performance.
- **Predefined Prompts:** Offers a set of predefined questions for quick queries.
- **Custom Wishes:** Users can input their custom queries to receive detailed answers.
- **Wish History:** Tracks user interactions with a history of wishes and responses.
- **Responsive Design:** Styled with HTML and CSS for an engaging user interface.
- **Optimized Performance:** Utilizes a quantized model (INT4) for efficient CPU usage.

---

## Requirements

Ensure the following are installed on your system:

- **Python 3.8+**
- **Streamlit 1.14.0+**
- **OpenVINO GenAI**
- **llm_config** (custom module for model configuration)
- Required Python libraries:
  - `streamlit`
  - `openvino-genai`
  - `pathlib`
  - `time`

---

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/your-username/aladdin-app.git](https://github.com/TABREZ-96/Aladdin)
   cd aladdin-app
