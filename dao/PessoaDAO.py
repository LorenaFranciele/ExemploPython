from model.Pessoa import Pessoa

class PessoaDAO:
  conexao = None
  cursor  = None

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor  = cur

  #getAll() quando for chamado, vai chamar todas as pessoas da tabela Pessoa lá no sqlite, criar um objeto para cada uma e retornar uma lista!!!
  def getAll(self):
    sql = "SELECT id, nome FROM pessoa"
   
    try:
     self.cursor.execute(sql)
     resultado = self.cursor.fetchall()
  #estamos criando uma lista para guardar um objeto do tipo Pessoa
     pessoas = []
     for linha in resultado:
      pessoa = Pessoa(linha[0], linha[1])
      #estamos adicionando cada um desses objetos Pessoa
      pessoas.append(pessoa)

     return pessoas
    except Exception as e:
      return e