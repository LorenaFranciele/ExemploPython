class Pessoa:
  # Atributos
  __id   = None
  __nome = None

  # Método Construtor
  def __init__(self, id, nome):
    self.__id   = id
    self.__nome = nome


# Método __str__: com ele, podemos ver o conteúdo do objeto mais fácil...
  def __str__(self):
   return f"{self.__nome} - ({self.__id})" 