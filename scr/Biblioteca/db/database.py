import sqlite3

def get_connection():
    conn = sqlite3.connect('biblioteca_0.db')
    return conn

def create_tables():
    conn = sqlite3.connect("biblioteca_0.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano_lancamento INTEGER,
            emprestado BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
