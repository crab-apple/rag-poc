import os
from uuid import UUID

from sqlalchemy import create_engine, text

from models import Position, User


def get_engine():
    return create_engine(os.environ["DATABASE_URL"])


def clear_data(conn) -> None:
    conn.execute(text("TRUNCATE TABLE positions, users RESTART IDENTITY CASCADE"))


def insert_users(conn, users: list[User]) -> None:
    for user in users:
        conn.execute(
            text("INSERT INTO users (id, name) VALUES (:id, :name)"),
            {"id": str(user.id), "name": user.name},
        )
        for position in user.employment_history:
            conn.execute(
                text(
                    "INSERT INTO positions (user_id, company, title)"
                    " VALUES (:user_id, :company, :title)"
                ),
                {"user_id": str(user.id), "company": position.company, "title": position.title},
            )


def insert_connections(conn, connections: list[tuple[UUID, UUID]]) -> None:
    conn.execute(
        text("INSERT INTO connections (user_id_1, user_id_2) VALUES (:u1, :u2)"),
        [{"u1": str(u1), "u2": str(u2)} for u1, u2 in connections],
    )


def fetch_users(conn, limit: int) -> list[User]:
    user_rows = conn.execute(
        text("SELECT id, name FROM users ORDER BY id LIMIT :limit"),
        {"limit": limit},
    ).fetchall()

    if not user_rows:
        return []

    user_ids = [row.id for row in user_rows]
    position_rows = conn.execute(
        text("SELECT user_id, company, title FROM positions WHERE user_id = ANY(:ids)"),
        {"ids": user_ids},
    ).fetchall()

    positions_by_user: dict[int, list[Position]] = {}
    for row in position_rows:
        positions_by_user.setdefault(row.user_id, []).append(
            Position(company=row.company, title=row.title)
        )

    return [
        User(id=UUID(str(row.id)), name=row.name, employment_history=positions_by_user.get(row.id, []))
        for row in user_rows
    ]
