import streamlit as st
from utils.openai_helper import generate_test_cases

# Title
st.title("🧪 AI Test Case Generator")

# Sidebar for Azure Config
st.sidebar.header("🔐 Azure OpenAI Configuration")

api_key = st.sidebar.text_input("API Key", type="password")
endpoint = st.sidebar.text_input("Endpoint URL")
deployment = st.sidebar.text_input("Deployment Name (e.g. gpt-4.1-mini)")

# Main Inputs
st.header("📋 Enter Story Details")

story = st.text_area("Story Description", height=150)
acceptance = st.text_area("Acceptance Criteria", height=150)

# Button
if st.button("🚀 Generate Test Cases"):

    if not api_key or not endpoint or not deployment:
        st.error("Please enter Azure details")
    elif not story or not acceptance:
        st.error("Please enter Story & Acceptance Criteria")
    else:
        with st.spinner("Generating test cases..."):

            result = generate_test_cases(
                api_key,
                endpoint,
                deployment,
                story,
                acceptance
            )

            st.success("✅ Test Cases Generated")

            st.text_area("📄 Output", result, height=400)

            # Download option
            st.download_button(
                label="⬇ Download Test Cases (csv)",
                data=result,
                file_name="test_cases.csv",
                mime="text/csv"
            )