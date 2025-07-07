class Livro:
    def __init__(self, id=None, titulo="", autor="", genero="", ano_lancamento=0, emprestado=False):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.emprestado = emprestado
