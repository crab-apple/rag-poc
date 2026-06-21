import anthropic

from embeddings import profile_to_text
from models import User

_MODEL_NAME = "claude-sonnet-4-6"

_client = anthropic.Anthropic()


def generate_answer(query: str, matches: list[User]) -> str:
    context = "\n".join(f"- {profile_to_text(user)}" for user in matches)
    prompt = (
        "Answer the question using only the user profiles below as context.\n\n"
        f"Profiles:\n{context}\n\n"
        f"Question: {query}"
    )
    response = _client.messages.create(
        model=_MODEL_NAME,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
