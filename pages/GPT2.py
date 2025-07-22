import streamlit as st
import requests


API_URL = "https://bd689eae75bc.ngrok-free.app/generate_gpt"

st.title("LSTM Text Generation")

st.subheader("GPT-2 Text Generation")
prompt = st.text_area("Enter prompt:", "The future of AI is")
    
max_length = st.slider("Max Length", 50, 500, 100)
temperature = st.slider("Temperature (Creativity)", 0.5, 1.5, 0.9, 0.1)
top_k = st.slider("Top-K Filtering", 10, 100, 40)
top_p = st.slider("Top-P Nucleus Sampling", 0.5, 1.0, 0.85, 0.05)

if st.button("Generate Text"):
        try:
            response = requests.post(API_URL, json={
                "prompt": prompt,
                "max_length": max_length,
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p
            },verify=False)
            result = response.json()
            if "generated_text" in result:
                st.success("Generated Text:")
                st.write(result["generated_text"])
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Request failed: {str(e)}")
