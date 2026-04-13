from openai import AzureOpenAI

def generate_test_cases(api_key, endpoint, deployment, story, acceptance):

    try:
        # Create Azure OpenAI client
        client = AzureOpenAI(
            api_key=api_key,
            api_version="2024-02-15-preview",
            azure_endpoint=endpoint
        )

        # Prompt (VERY IMPORTANT)
        prompt = f"""
        You are a Senior QA Automation Engineer.

Your task is to generate test cases for the given user story.

APPLICATION CONTEXT:
This application is related to chatbot answer validation. The goal is to ensure that the chatbot provides accurate, relevant, clear, and polite responses.

USER STORY:
{story}

ACCEPTANCE CRITERIA:
{acceptance}

INSTRUCTIONS:
- Generate EXACTLY 5 test cases
- Include positive, negative, and edge cases
- Keep steps clear and structured

OUTPUT FORMAT (STRICT CSV):
Do NOT add any explanation.
Do NOT ask questions.
Return ONLY in CSV format as shown below.

Test Case ID,Objective,Precondition,Test Steps,Expected Result

TC_001,Verify valid response,User asks valid question,"1. Open chatbot\n2. Ask valid query",Chatbot gives accurate answer
"""

        # Call API
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "You are a QA expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"