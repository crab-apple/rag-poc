import chromadb
from fastembed import TextEmbedding

from models import User

_MODEL_NAME = "BAAI/bge-small-en-v1.5"
_COLLECTION_NAME = "user_profiles"


def profile_to_text(user: User) -> str:
    if user.employment_history:
        roles = ", ".join(f"{p.title} at {p.company}" for p in user.employment_history)
        return f"{user.name}. Employment history: {roles}."
    return f"{user.name}."


def generate_and_store_embeddings(users: list[User]) -> None:
    model = TextEmbedding(_MODEL_NAME)
    client = chromadb.EphemeralClient()
    collection = client.get_or_create_collection(_COLLECTION_NAME)

    texts = [profile_to_text(u) for u in users]
    embeddings = list(model.embed(texts))

    collection.add(
        ids=[str(u.id) for u in users],
        embeddings=embeddings,
        documents=texts,
    )
    print(f"Stored embeddings for {len(users)} users.")
