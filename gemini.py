import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception(f"GEMINI_API_KEY not found. Looking for .env at: {env_path}")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_reply(user_message, recommendations):
    try:
        if recommendations:
            recommendation_text = "\n".join(
                [
                    f"- {item['name']}: {item['url']}"
                    for item in recommendations
                ]
            )
        else:
            recommendation_text = "No assessments found."

        prompt = f"""
You are an SHL Assessment Recommendation Assistant.

User Query:
{user_message}

Recommended Assessments:
{recommendation_text}

Write a short professional response explaining why these assessments are suitable.
Do not invent assessments.
Keep the response under 120 words.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"