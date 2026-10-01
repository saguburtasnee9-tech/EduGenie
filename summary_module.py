from qna import client


def summarize_text(text: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(
            "Summarize the following text clearly and briefly for a student. "
            "Keep the important points and make the summary easy to understand.\n\n"
            f"Text:\n{text}"
        )
    )

    return response.text