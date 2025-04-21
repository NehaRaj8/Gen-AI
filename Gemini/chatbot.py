import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# load dotenv
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

#streamlit app header
st.header ("Generative AI Chatbot")

#select the model version

model_name = st.selectbox("Select Gemini Model",["gemini-1.5-pro", "gemini-1.5-flash"])

# initilize the gemini model

model = genai.GenerativeModel(model_name)

# user input

user_input = st.text_input("Enter your question")

#Button to trigger summarization
if st.button("Start"):
    if user_input.strip():
        try:
            result = model.generate_content(user_input)
            st.write(result.text)
        except Exception as e:
            st.write(f"An error occured : {str(e)}")   
    else: st.warning("Please entre a question") 
