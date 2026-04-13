# AI Test Case Generator

A Streamlit-based web application that leverages **Azure OpenAI** to automatically generate comprehensive test cases from user stories and acceptance criteria. This tool helps QA teams and developers streamline test planning by converting narrative requirements into structured, actionable test scenarios.

## 🚀 Features

- **AI-Powered Generation**: Uses Azure OpenAI's GPT models to create detailed test cases based on input descriptions.
- **User-Friendly Interface**: Simple web UI built with Streamlit for easy input and output.
- **CSV Export**: Download generated test cases as a CSV file for integration with test management tools.
- **Configurable**: Supports custom Azure OpenAI deployments for flexibility.
- **Real-Time Feedback**: Provides status spinners and success messages during the generation process.

## 📋 Prerequisites

Before running the application, ensure you have:

*   **Python 3.8** or higher
*   An active **Azure OpenAI account** with:
    *   API Key
    *   Endpoint URL
    *   Deployment Name (e.g., `gpt-4` or `gpt-4-turbo`)


