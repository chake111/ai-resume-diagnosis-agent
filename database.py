import sqlite3
from datetime import datetime


def init_db():
    with sqlite3.connect("resume_agent.db") as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS diagnosis_history
                     (
                         id               INTEGER PRIMARY KEY AUTOINCREMENT,
                         user_id          INTEGER,
                         session_id       TEXT,
                         target_role      TEXT,
                         resume_text      TEXT,
                         diagnosis_result TEXT,
                         created_at       TEXT
                     )
                     """)


def save_diagnosis(user_id, session_id, role, resume, result):
    with sqlite3.connect("resume_agent.db") as conn:
        conn.execute("""
                     INSERT INTO diagnosis_history
                     (user_id, session_id, target_role, resume_text,
                      diagnosis_result, created_at)
                     VALUES (?, ?, ?, ?, ?, ?)
                     """, (user_id, session_id, role, resume, result,
                           datetime.now().isoformat()))


def get_recent_diagnoses(limit=10):
    with sqlite3.connect("resume_agent.db") as conn:
        return conn.execute("""
                     SELECT id,
                            user_id,
                            session_id,
                            target_role,
                            resume_text,
                            diagnosis_result,
                            created_at
                     FROM diagnosis_history
                     ORDER BY id DESC
                     LIMIT ?
                     """, (limit,)).fetchall()
