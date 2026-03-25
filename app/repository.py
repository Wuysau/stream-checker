from app.db import creat_connection
from app.models import CheckStatus


def create_check_tast(started_at: str) -> int:
    conn = creat_connection()
    try:
        cu = conn.cursor()
        cu.execute("INSERT INTO check_tasks (started_at) VALUES (?)", (started_at,))
        conn.commit()
        return cu.lastrowid
    finally:
        conn.close()
