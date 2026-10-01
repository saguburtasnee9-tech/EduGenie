from qna import client


def recommend_learning_path(topic: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(
            f"Create a personalized learning path for a student who wants "
            f"to learn: {topic}\n\n"
            "Give the learning path in clear steps, starting from the "
            "basics and gradually moving to advanced topics."
        )
    )

    return response.text