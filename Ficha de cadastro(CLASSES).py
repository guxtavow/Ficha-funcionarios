#classes são agrupadores de funções e dados(def)
#classe (categoria)
#objetos(subcategorias)
from funcoes.Login import Entrar,Criar_senha,senhasSQL
from datetime import datetime

def Empresa():
  #FUNCIONÁRIOS
    x1 = "1"
    x2 = "2"
    x3 = "3"

    decisao = input("O que você quer saber sobre os funcionarios?\n1.Nome completo\n2.Idade\n3.Ficha Completa\nDigite o numero: ")
  
    if decisao == x1:
      print(user1.nomecompleto())
      print(user2.nomecompleto())
      print(user3.nomecompleto())
      print()
      return Empresa()

    elif decisao == x2:
      print(user1.idades())
      print(user2.idades())
      print(user3.idades())
      print()
      return Empresa()

    elif decisao == x3:
      print(user1.fichacompleta())
      print(user2.fichacompleta())
      print(user3.fichacompleta())
      print()
      return Empresa()
    
    else:
      print("Opção invalida, tente novamente!!")
      return Empresa()

class Funcionarios: #Criar classes é mais util para FUNÇÕES e não DADOS
  def __init__ (self,nome,sobrenome, nascimento,idade): #Construtor(Sempre colocar). Self = suprir nome do USER1
    self.nome = nome #definiu-se nome 
    self.sobrenome = sobrenome#definiu-se sobrenome
    self.nascimento = nascimento #definiu-se nascimento
    self.idade = idade #definiu-se idade
  def nomecompleto (self):
    return(self.nome + " " + self.sobrenome)
  def nomeidade (self):
    return(self.nome + ", nascida em: " + self.nascimento)
  def idades (self):
    anoatual = datetime.now().year
    self.idade = int(anoatual - self.idade)
    self.idade = str(self.idade)
    return (self.nome + " tem "+ str(self.idade) +" anos")
  def fichacompleta (self):
    ano = datetime.now().year
    idade = ano - self.idade
    idade = str(idade)
    return(self.nome + " " + self.sobrenome + ", "+ idade + " anos, nascido em: " + self.nascimento)
  
# Passar os parametros
user1 = Funcionarios ("Pedro", "Souza","01/01/1990",1990)
user2 = Funcionarios ("Maria","Eduarda","11/10/2001",2001)
user3 = Funcionarios ("Miguel", "Andrade","25/07/2002",2002)

senhasSQL()

#CADASTRO
y1 = "1"
y2 = "2"

def decisoes():
  print()
  decisao0 = input("Primeiramente, faça login ou cadastre-se:\n1.Fazer Login\n2.Cadastrar\nDigite o numero: ")
  if decisao0 == y1:
    if Entrar() == True:
      print()
      Empresa()
    else:
      print("Senha incorreta. Tente novamente")
      print()
      return decisoes()
  elif decisao0 == y2:
    Criar_senha()
    if Entrar() == True:
      print()
      Empresa()
    else:
      print("Senha incorreta. Tente novamente")
      print()
      return decisoes()
  else:
    print("Opa! Parece que você digitou uma opção que não existe. Tente novamente.")
    print()
    return decisoes()

print()
print("Bem-vindo a lista funcionários.")
decisoes()