#classes são agrupadores de funções e dados(def)
#classe (categoria)
#objetos(subcategorias)
from funcoes.Login import Entrar,Criar_senha
from datetime import datetime

print()
print("Bem-vindo a lista funcionários.")
print()

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

for xy in range(3):

#CADASTRO
  y1 = "1"
  y2 = "2"

#FUNCIONÁRIOS
  x1 = "1"
  x2 = "2"
  x3 = "3"

  decisao0 = input("Primeiramente, faça login ou cadastre-se:\n1.Fazer Login\n2.Cadastrar\nDigite o numero: ")
  if decisao0 == y1:
    Entrar()
    print()
  elif decisao0 == y2:
    Criar_senha()
  else:
    print(" Opa! Parece que você digitou uma opção que não existe. Tente novamente.")
    break

    


#SABER FUNCIONÁRIOS
  decisao = input("O que você quer saber sobre os funcionarios?\n1.Nome completo\n\n2.Idade\n\n3.Ficha Completa\n\nDigite o numero: ")

  if decisao == x1:
    print(user1.nomecompleto())
    print(user2.nomecompleto())
    print(user3.nomecompleto())
    print()

  elif decisao == x2:
    print(user1.idades())
    print(user2.idades())
    print(user3.idades())
    print()

  elif decisao == x3:
    print(user1.fichacompleta())
    print(user2.fichacompleta())
    print(user3.fichacompleta())
    print()
  else:
    print("Opção invalida, tente novamente!!")
    print()
    
