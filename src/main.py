from alembic import command
from alembic.config import Config

from db import clear_data, fetch_users, get_engine, insert_connections, insert_users
from embeddings import generate_and_store_embeddings, get_model, search_similar_users
from generation import generate_answer
from sample_data import generate_connections, generate_users


def run_migrations() -> None:
    command.upgrade(Config("alembic.ini"), "head")


def run_search_loop(users, model, collection) -> None:
    users_by_id = {str(user.id): user for user in users}

    print("\nEnter a search query and press Enter (empty line to quit).")
    while True:
        try:
            query = input("\nSearch> ").strip()
        except EOFError:
            break
        if not query:
            break

        matches = search_similar_users(collection, model, query, n_results=3)
        matched_users = [users_by_id[user_id] for user_id, _ in matches]

        print(f"Top {len(matches)} matches for {query!r}:")
        for rank, (user, (_, distance)) in enumerate(zip(matched_users, matches), start=1):
            roles = ", ".join(f"{p.title} at {p.company}" for p in user.employment_history)
            print(f"  {rank}. {user.name} (distance={distance:.4f}) - {roles}")

        print(f"\nAnswer: {generate_answer(query, matched_users)}")


if __name__ == "__main__":
    run_migrations()

    engine = get_engine()
    users = generate_users(1000)

    with engine.begin() as conn:
        clear_data(conn)
        insert_users(conn, users)
        connections = generate_connections(users)
        insert_connections(conn, connections)

    print(f"Saved {len(users)} users and {len(connections)} connections.")

    model = get_model()
    collection = generate_and_store_embeddings(users, model)
    run_search_loop(users, model, collection)
