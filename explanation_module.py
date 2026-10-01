from qna import client


def explain_topic(topic: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(
            f"Explain the following topic to a student in simple, "
            f"easy-to-understand language. Use examples where helpful.\n\n"
            f"Topic: {topic}"
        )
    )

    return response.text