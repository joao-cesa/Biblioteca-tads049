from scr.Biblioteca.Service import livro_service

def importar_livros(query):
    livro_service.importar_livros_google(query)
def adicionar_livro(titulo, autor, genero, ano):
    return livro_service.cadastrar_livro(titulo, autor, genero, ano)

def buscar_livros(filtro, campo):
    return livro_service.pesquisar_livros(filtro, campo)

def emprestar_livro(livro_id):
    livro_service.solicitar_emprestimo(livro_id)

def excluir_livro(livro_id):
    livro_service.remover_livro(livro_id)

def devolver_livro(livro_id):
    livro_service.devolver_livro(livro_id)
