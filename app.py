
import os
from openai import OpenAI

# Set SPUR-compatible inference endpoint and API key
base_url = os.environ.get("SPUR_BASE_URL")
api_key = os.environ.get("SPUR_API_KEY")
model = os.environ.get("SPUR_MODEL")

def answer_question(context, question):
    if not base_url or not api_key or not model:
        return "Setup required: configure SPUR_BASE_URL, SPUR_API_KEY, and SPUR_MODEL."

    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    response = client.chat.completions.create(
        model=model,
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer using only the supplied document context. "
                    "If the answer is missing, say you cannot find it in the document."
                )
            },
            {
                "role": "user",
                "content": f"Document context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    sample_context = (
        "The library opens at 9 AM and closes at 5 PM. "
        "It is closed on Sundays."
    )
    question = input("Ask a question about the sample document: ")
    print(answer_question(sample_context, question))
