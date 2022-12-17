# Importar a biblioteca que acessa o SQLite.. chama "sqlite3"
# para instalar, pip install sqlite3
import sqlite3

class Database:
    #Atributos
    conexao = None
    cursor  = None

    #Método construtor
    def __init__(self):
        self.conexao = sqlite3.connect("database/imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.conexao.commit()
