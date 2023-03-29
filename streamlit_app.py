#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]

def explain_code(input_string): 
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt="Explain this code: " + input_string +"\n",
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop=["\"\"\""],
    )
    answer = response.choices[0].text.strip()
    return answer

# Define the Streamlit app
def app():
    st.header("Welcome to Code Demystify")
    st.subheader("Louie F. Cervantes M.Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("Code Demystify will explain complicated code")
    
    # Create a multiline text field
    user_input = st.text_area('Paste a block of code', height=10)

    # Display the text when the user submits the form
    if st.button('Submit'):
        output = explain_code(user_input)
        st.write(output)

# Run the app
if __name__ == "__main__":
    app()
