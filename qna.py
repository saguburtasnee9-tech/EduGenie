import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def answer_question(question: str) -> str:
    response = client.models.generate_content(
          model="gemini-3.5-flash-lite",
        contents=f"Answer this student's question clearly and simply:\n\n{question}"
    )

    return response.text