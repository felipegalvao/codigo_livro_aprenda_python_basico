# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 13: Programação Orientada a Objetos

# Definindo nossa primeira classe
class Usuario:
  contador = 0

  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    Usuario.contador += 1

  def diga_ola(self):
    print("Olá, meu nome é %s e meu email é %s" % (self.nome, self.email))

# Criando o primeiro objeto da classe
usuario1 = Usuario(nome="Felipe", email="contato@felipegalvao.com.br")

usuario1.diga_ola()
print(usuario1.nome)

# Alterando propriedade do objeto
usuario1.nome = "Felipe Galvão"
print(usuario1.nome)

# Funções para alterar, recuperar e deletar uma propriedade
print(hasattr(usuario1, "nome"))
print(hasattr(usuario1, "idade"))
print(getattr(usuario1, "email"))
setattr(usuario1, "nome", "Felipe G.")
setattr(usuario1, "idade", 30)
print(getattr(usuario1, "nome"))
print(getattr(usuario1, "idade"))
delattr(usuario1, "idade")
# print(getattr(usuario1, "idade"))

# Variável de classe - contador
usuario2 = Usuario(nome="Jurema", email="jurema@jurema.com")
print(Usuario.contador)

# Herança - Definição de uma classe estendida a partir de outra classe
class Administrador(Usuario):
  def __init__(self, nome, email, chave_de_administrador):
    Usuario.__init__(self, nome, email)
    self.chave_de_administrador = chave_de_administrador


  def poder_administrativo(self):
    print("Eu tenho o poder! Minha chave é %s" % self.chave_de_administrador)


usuario_adm = Administrador(nome="Admin", email="admin@admin.com", chave_de_administrador="123456")
usuario_adm.diga_ola()
usuario_adm.poder_administrativo()

# Nova classe, sobrescrevendo o método diga_ola da classe original
class MembroStaff(Usuario):
  def __init__(self, nome, email):
    Usuario.__init__(self, nome, email)

  def diga_ola(self):
    print("Olá, meu nome é %s e eu sou membro do Staff. Em que posso ajudar?" % (self.nome))

membro_staff_1 = MembroStaff(nome="Mariazinha", email="maria@zinha.com.br")
membro_staff_1.diga_ola()