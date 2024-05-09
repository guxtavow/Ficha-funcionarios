import bcrypt
import time
import sys

def Entrar():
    try:    
        def checar_senha(checagem, hash_senha):
            return bcrypt.checkpw(checagem.encode('utf-8'),hash_senha)

        pergunta2 = input("Digite a senha criada: ")
        if checar_senha(pergunta2, Criar_senha):
            print('Senha está correta.')
        else:
            print("Senha incorreta.")
            
    except:
        print("Parece que você não está cadastrado!")
        Cadastro = input("Deseja se cadastrar? \n.Sim\n.Não\nDigite APENAS sim ou não: ").upper()
        if Cadastro == "SIM":
            print("Perfeito! Então vamos dar prosseguimento. Primeiramente:")
            Criar_senha()
        elif Cadastro == "NAO": 
            print("Tudo bem então, até mais!")
            sys.exit(1)
        else:
            print("LEMBRETE: Só é aceitavel SIM ou NAO como resposta!")
            sys.exit(1)

        

def Criar_senha():
    pergunta = input("Digite uma senha: ")

    senha = pergunta.encode('utf-8')
    key = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha,key)
    print("Senha criada")
    print()
    time.sleep(1.5)