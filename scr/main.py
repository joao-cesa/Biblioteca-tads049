import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox
)
from scr.Biblioteca.Controller import livro_controller
from scr.Biblioteca.db.database import create_tables

class BibliotecaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteca (PyQt)")
        self.setGeometry(100, 100, 1000, 600)
        self.setup_ui()
        create_tables()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Estilo geral
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: Arial;
            }
            QLineEdit {
                padding: 4px;
                background-color: #444;
                color: #fff;
                border: 1px solid #666;
                border-radius: 4px;
            }
            QComboBox {
                padding: 4px;
                background-color: #444;
                color: #fff;
                border: 1px solid #666;
                border-radius: 4px;
            }
            QTableWidget {
                background-color: #383838;
                color: #ffffff;
            }
            QHeaderView::section {
                background-color: #555;
                color: #fff;
                font-weight: bold;
            }
            QPushButton {
                font-weight: bold;
                border-radius: 5px;
                padding: 6px;
            }
        """)

        # Campos de cadastro
        form_layout = QHBoxLayout()
        self.titulo_input = QLineEdit()
        self.autor_input = QLineEdit()
        self.genero_input = QLineEdit()
        self.ano_input = QLineEdit()

        form_layout.addWidget(QLabel("Título"))
        form_layout.addWidget(self.titulo_input)
        form_layout.addWidget(QLabel("Autor"))
        form_layout.addWidget(self.autor_input)
        form_layout.addWidget(QLabel("Gênero"))
        form_layout.addWidget(self.genero_input)
        form_layout.addWidget(QLabel("Ano"))
        form_layout.addWidget(self.ano_input)

        layout.addLayout(form_layout)

        # Botão de cadastrar
        btn_cadastrar = QPushButton("Cadastrar Livro")
        btn_cadastrar.clicked.connect(self.cadastrar_livro)
        btn_cadastrar.setStyleSheet("background-color: #007acc; color: white;")
        layout.addWidget(btn_cadastrar)

        # Pesquisa
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_field = QComboBox()
        self.search_field.addItems(["titulo", "autor", "genero", "ano_lancamento"])

        btn_buscar = QPushButton("Buscar")
        btn_buscar.clicked.connect(self.buscar_livros)
        btn_buscar.setStyleSheet("background-color: #555; color: white;")

        btn_importar = QPushButton("Importar Google Books")
        btn_importar.clicked.connect(self.importar_google)
        btn_importar.setStyleSheet("background-color: #555; color: white;")

        search_layout.addWidget(QLabel("Pesquisar"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(btn_buscar)
        search_layout.addWidget(btn_importar)

        layout.addLayout(search_layout)

        # Tabela
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Título", "Autor", "Gênero", "Ano", "Status"])
        layout.addWidget(self.table)

        # Botões de ação
        action_layout = QHBoxLayout()

        btn_emprestar = QPushButton("Emprestar")
        btn_emprestar.clicked.connect(self.emprestar)
        btn_emprestar.setStyleSheet("background-color: #28a745; color: white;")

        btn_devolver = QPushButton("Devolver")
        btn_devolver.clicked.connect(self.devolver)
        btn_devolver.setStyleSheet("background-color: #ffc107; color: black;")

        btn_excluir = QPushButton("Excluir")
        btn_excluir.clicked.connect(self.excluir)
        btn_excluir.setStyleSheet("background-color: #dc3545; color: white;")

        action_layout.addWidget(btn_emprestar)
        action_layout.addWidget(btn_devolver)
        action_layout.addWidget(btn_excluir)

        layout.addLayout(action_layout)

        self.setLayout(layout)

    def cadastrar_livro(self):
        titulo = self.titulo_input.text()
        autor = self.autor_input.text()
        genero = self.genero_input.text()
        ano = self.ano_input.text()

        if not (titulo and autor and genero and ano):
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos")
            return

        livro_controller.adicionar_livro(titulo, autor, genero, int(ano))
        QMessageBox.information(self, "Sucesso", "Livro cadastrado!")
        self.clear_fields()
        self.buscar_livros()

    def buscar_livros(self):
        filtro = self.search_input.text()
        campo = self.search_field.currentText()

        livros = livro_controller.buscar_livros(filtro, campo)
        self.table.setRowCount(0)

        for livro in livros:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            self.table.setItem(row_pos, 0, QTableWidgetItem(str(livro.id)))
            self.table.setItem(row_pos, 1, QTableWidgetItem(livro.titulo))
            self.table.setItem(row_pos, 2, QTableWidgetItem(livro.autor))
            self.table.setItem(row_pos, 3, QTableWidgetItem(livro.genero))
            self.table.setItem(row_pos, 4, QTableWidgetItem(str(livro.ano_lancamento)))
            status = "Emprestado" if livro.emprestado else "Disponível"
            self.table.setItem(row_pos, 5, QTableWidgetItem(status))

    def importar_google(self):
        termo = self.search_input.text()
        if not termo:
            QMessageBox.warning(self, "Aviso", "Digite um termo para importar")
            return
        livro_controller.importar_livros(termo)
        QMessageBox.information(self, "Sucesso", f"Livros importados com termo: {termo}")
        self.buscar_livros()

    def emprestar(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Aviso", "Selecione um livro")
            return
        livro_id = int(self.table.item(row, 0).text())
        status = self.table.item(row, 5).text()

        if status == "Emprestado":
            QMessageBox.warning(self, "Aviso", "Livro já emprestado")
            return

        livro_controller.emprestar_livro(livro_id)
        QMessageBox.information(self, "Sucesso", "Livro emprestado!")
        self.buscar_livros()

    def devolver(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Aviso", "Selecione um livro")
            return
        livro_id = int(self.table.item(row, 0).text())
        status = self.table.item(row, 5).text()

        if status == "Disponível":
            QMessageBox.warning(self, "Aviso", "Livro já está disponível")
            return

        livro_controller.devolver_livro(livro_id)
        QMessageBox.information(self, "Sucesso", "Livro devolvido!")
        self.buscar_livros()

    def excluir(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Aviso", "Selecione um livro")
            return
        livro_id = int(self.table.item(row, 0).text())

        confirm = QMessageBox.question(self, "Confirmar", "Deseja realmente excluir?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            livro_controller.excluir_livro(livro_id)
            QMessageBox.information(self, "Sucesso", "Livro excluído!")
            self.buscar_livros()

    def clear_fields(self):
        self.titulo_input.clear()
        self.autor_input.clear()
        self.genero_input.clear()
        self.ano_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BibliotecaApp()
    window.show()
    sys.exit(app.exec_())
