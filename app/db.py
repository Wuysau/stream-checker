import sqlite3
from pathlib import Path

DB_FILE = Path("data/stream_checker.db")


def creat_connection() -> sqlite3.Connection:
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)

    cx = sqlite3.connect(str(DB_FILE))
    cx.row_factory = sqlite3.Row
    return cx


# 3/17-3/21 单词日50（明天加100 只用零散时间）写自己的项目 健身房3天 数学写了几道题 周末朋友来上海，玩两天 出差时间被压缩，大部分花在项目上，下周合理分配
def init_DB() -> None:
    conn = creat_connection()
    try:
        cu = conn.cursor()
        cu.execute(
            """
            CREATE TABLE IF NOT EXISTS check_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                total_count INTEGER DEFAULT 0,
                success_count INTEGER DEFAULT 0,
                failed_count INTEGER DEFAULT 0,
                success_rate REAL DEFAULT 0,
                avg_response_time_ms REAL DEFAULT 0
            )
            """
        )

        cu.execute(
            """
            CREATE TABLE IF NOT EXISTS check_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                channel_name TEXT NOT NULL,
                channel_url TEXT NOT NULL,
                status TEXT NOT NULL,
                status_code INTEGER,
                response_time_ms INTEGER,
                error TEXT,
                checked_at TEXT NOT NULL,
                FOREIGN KEY(task_id) REFERENCES check_tasks(id)
            )
            """
        )
        conn.commit()
    finally:
        conn.close()
