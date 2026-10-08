import streamlit as st

from prompt import compare_prompts
from llm import get_response


# Page configuration
st.set_page_config(
    page_title="Prompt Comparison",
    page_icon="🤖",
    layout="wide"
)


# Title
st.title("🤖 Prompt Comparison")
st.write("Compare different prompting techniques using an LLM.")


# User input
topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Artificial Intelligence"
)


# Generate button
if st.button("Generate Responses"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        # Generate prompts
        prompts = compare_prompts(topic)

        st.subheader("Prompt Comparison")

        # Create columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Basic Prompt")
            st.code(prompts["Basic Prompt"])

        with col2:
            st.markdown("### Detailed Prompt")
            st.code(prompts["Detailed Prompt"])

        with col3:
            st.markdown("### Structured Prompt")
            st.code(prompts["Structured Prompt"])

        st.divider()

        # Generate LLM responses
        st.subheader("LLM Responses")

        for prompt_name, prompt_text in prompts.items():

            st.markdown(f"### {prompt_name}")

            with st.spinner(f"Generating response for {prompt_name}..."):
                response = get_response(prompt_text)

            st.write(response)

            st.divider()