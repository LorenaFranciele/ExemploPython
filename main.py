# Importa nosso arquivo Pessoa.py no diretório model/
from model.Pessoa import Pessoa

# precisa importar o Database e o PessoaDAO
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# Instanciando um objeto do tipo Pessoa no Python...
lorena = Pessoa(1,"Lorena Franciele")

# O atributo está privado..aqui dá erro...
# print(lorena.__nome)
print(lorena)

# a partir de agora, vamos para o acesso a banco
print("ACESSO A BANCO.....")
# chama o objeto de banco de dados
db = Database()

# Instancia um objeto do tipo PessoaDAO
pessoaDAO = PessoaDAO(db.conexao,db.cursor)

#quero exibir na tela todos os atores, atrizes e diretores do banco....
pessoas = pessoaDAO.getAll()

for pessoa in pessoas:
  print(pessoa)
