# Importa nosso arquivo Pessoa.py no diretório model/
from model.Pessoa import Pessoa

# Instanciando um objeto do tipo Pessoa no Python...
lorena = Pessoa(1,"Lorena Franciele")
# O atributo está privado..aqui dá erro...
# print(lorena.__nome)
print(lorena)



