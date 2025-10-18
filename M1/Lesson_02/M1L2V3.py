# import packages
from dotenv import load_dotenv
import openai
import streamlit as st


# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Explain generative AI in one sentence."}  # Prompt
    ],
    temperature=0.7,  # A bit of creativity
    max_tokens=100  # Limit response length
)

# print the response from OpenAI
st.write(response.choices[0].message.content)