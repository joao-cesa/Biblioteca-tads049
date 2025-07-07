from scr.Biblioteca.db.database import get_connection
from scr.Biblioteca.Model.livro import Livro

def salvar_livro(livro: Livro):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO livros (titulo, autor, genero, ano_lancamento, emprestado)
        VALUES (?, ?, ?, ?, ?)
    """, (livro.titulo, livro.autor, livro.genero, livro.ano_lancamento, livro.emprestado))
    conn.commit()
    conn.close()

def buscar_livros(filtro="", campo="titulo"):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT id, titulo, autor, genero, ano_lancamento, emprestado FROM livros WHERE {campo} LIKE ?"
    cursor.execute(query, (f"%{filtro}%",))
    rows = cursor.fetchall()
    conn.close()
    return [Livro(*row) for row in rows]

def emprestar_livro(livro_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET emprestado = 1 WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()


def salvar_varios_livros(livros):
    conn = get_connection()
    cursor = conn.cursor()

    for livro in livros:
        cursor.execute("""
            INSERT INTO livros (titulo, autor, genero, ano_lancamento, emprestado)
            VALUES (?, ?, ?, ?, ?)
        """, (livro.titulo, livro.autor, livro.genero, livro.ano_lancamento, livro.emprestado))

    conn.commit()
    conn.close()

def excluir_livro(livro_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()

def devolver_livro(livro_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET emprestado = 0 WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()
