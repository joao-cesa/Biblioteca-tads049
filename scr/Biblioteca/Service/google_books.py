import requests
from scr.Biblioteca.Model.livro import Livro

def buscar_livros_google(query, max_results=20):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()

    livros = []
    if "items" in data:
        for item in data["items"]:
            volume_info = item.get("volumeInfo", {})
            titulo = volume_info.get("title", "Sem Título")
            autores = volume_info.get("authors", ["Desconhecido"])
            genero = volume_info.get("categories", ["Geral"])
            ano = volume_info.get("publishedDate", "0")[:4]

            try:
                ano_int = int(ano)
            except:
                ano_int = 0

            livro = Livro(
                titulo=titulo,
                autor=", ".join(autores),
                genero=genero[0] if genero else "Geral",
                ano_lancamento=ano_int,
                emprestado=False
            )
            livros.append(livro)
    return livros
