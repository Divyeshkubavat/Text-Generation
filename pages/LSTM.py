import streamlit as st
import requests

API_URL = "https://bd689eae75bc.ngrok-free.app/generate_lstm"

st.title("LSTM Text Generation")

# User inputs
seed_text = st.text_input("Enter seed text:", "Once upon a time")
word_count = st.number_input("Number of words to generate:", min_value=1, max_value=200, value=50)

if st.button("Generate Text"):
    try:
        response = requests.post(API_URL, json={"seed_text": seed_text, "next_words": word_count},verify=False)
        result = response.json()

        if "generated_text" in result:
            st.success(f"Generated Text:\n\n{result['generated_text']}")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")
