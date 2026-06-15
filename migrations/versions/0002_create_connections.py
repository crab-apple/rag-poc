from alembic import op

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE connections (
            user_id_1 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            user_id_2 UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            PRIMARY KEY (user_id_1, user_id_2),
            CHECK (user_id_1 < user_id_2)
        )
    """)


def downgrade() -> None:
    op.execute("DROP TABLE connections")
