from scr.Biblioteca.Model.livro import Livro
from scr.Biblioteca.Repository import livro_repository
from scr.Biblioteca.Service import google_books

def cadastrar_livro(titulo, autor, genero, ano_lancamento):
    livro = Livro(titulo=titulo, autor=autor, genero=genero, ano_lancamento=ano_lancamento)
    livro_repository.salvar_livro(livro)
    return livro

def pesquisar_livros(filtro, campo):
    return livro_repository.buscar_livros(filtro, campo)

def solicitar_emprestimo(livro_id):
    livro_repository.emprestar_livro(livro_id)

def importar_livros_google(query):
    livros = google_books.buscar_livros_google(query)
    livro_repository.salvar_varios_livros(livros)

def remover_livro(livro_id):
    livro_repository.excluir_livro(livro_id)

def devolver_livro(livro_id):
    livro_repository.devolver_livro(livro_id)

