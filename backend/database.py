import sqlite3

def init_db():
    conn = sqlite3.connect("ats.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER,
        missing_skills TEXT,
        strengths TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_result(score, missing_skills, strengths):
    conn = sqlite3.connect("ats.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO results (score, missing_skills, strengths)
    VALUES (?, ?, ?)
    """, (score, missing_skills, strengths))

    conn.commit()
    conn.close()

# Initialize database on import
init_db()
