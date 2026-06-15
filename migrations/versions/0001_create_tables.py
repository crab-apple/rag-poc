from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE users (
            id   UUID PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    op.execute("""
        CREATE TABLE positions (
            id      SERIAL PRIMARY KEY,
            user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            company TEXT NOT NULL,
            title   TEXT NOT NULL
        )
    """)


def downgrade() -> None:
    op.execute("DROP TABLE positions")
    op.execute("DROP TABLE users")
