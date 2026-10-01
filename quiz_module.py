from qna import client


def generate_quiz(topic: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(
            f"Create a short educational quiz for a student about: {topic}\n\n"
            "Include 5 multiple-choice questions. "
            "Give 4 options (A, B, C, D) for each question and clearly "
            "show the correct answer after each question."
        )
    )

    return response.text