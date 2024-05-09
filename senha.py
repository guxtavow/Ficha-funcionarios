import bcrypt
import time

pergunta = input("Digite uma senha: ")

senha = pergunta.encode('utf-8')
key = bcrypt.gensalt()
hash_senha = bcrypt.hashpw(senha,key)
print("Senha criada")

time.sleep(3)

def checar_senha(checagem, hash_senha):
    return bcrypt.checkpw(checagem.encode('utf-8'),hash_senha)

pergunta2 = input("Digite a senha criada: ")

if checar_senha(pergunta2, hash_senha):
    print('Senha está correta.')
else:
    print("Senha incorreta.")