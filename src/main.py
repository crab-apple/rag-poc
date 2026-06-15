from alembic import command
from alembic.config import Config

from db import clear_data, fetch_users, get_engine, insert_connections, insert_users
from sample_data import generate_connections, generate_users


def run_migrations() -> None:
    command.upgrade(Config("alembic.ini"), "head")


if __name__ == "__main__":
    run_migrations()

    engine = get_engine()
    users = generate_users(1000)

    with engine.begin() as conn:
        clear_data(conn)
        insert_users(conn, users)
        connections = generate_connections(users)
        insert_connections(conn, connections)
        first_ten = fetch_users(conn, 10)

    print(f"Saved {len(users)} users and {len(connections)} connections. First 10 from DB:\n")
    for user in first_ten:
        print(f"  {user.name}")
        for position in user.employment_history:
            print(f"    {position.title} at {position.company}")
