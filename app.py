from langchain_community.llms import Ollama
import streamlit as st
import time

# Initialize the LLM
llm = Ollama(model="llama3")

st.title("Chatbot using Llama3")

# Input field for the prompt
prompt = st.text_area("Enter your prompt:")

# Button to trigger generation
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            # Create a placeholder for dynamic content
            placeholder = st.empty()

            # Iterate over the generator and update the placeholder
            try:
                for chunk in llm.stream(prompt, stop=['']):
                    placeholder.write(chunk)
                    # Optionally add a short delay to simulate real-time streaming
                    time.sleep(0.1)  # Adjust sleep time if needed
            except Exception as e:
                st.error(f"An error occurred: {e}")
