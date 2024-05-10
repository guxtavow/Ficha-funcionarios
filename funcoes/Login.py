import bcrypt
import time
import sys
import sqlite3

def senhasSQL():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hash_senha TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def Criar_senha():
    pergunta = input("Digite uma senha: ")

    senha = pergunta.encode('utf-8')
    key = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha,key)

#INSERIR SENHA NO SQL
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    try:
        # Hash da senha usando bcrypt
        cursor.execute('INSERT INTO senhas (hash_senha) VALUES (?)', (hash_senha.decode('utf-8'),))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Senha já existe no banco de dados e foi ignorada.")
        return Entrar()
    finally:
        conn.close()

    print("Senha criada")
    print()
    time.sleep(1.5)



def Entrar():
    def verificar_senha(senha):    
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('SELECT hash_senha FROM senhas')
        senhas_hash = cursor.fetchall()
        conn.close()

        for hash_salva in senhas_hash:
            if bcrypt.checkpw(senha.encode('utf-8'), hash_salva[0].encode('utf-8')):
                return True
        return False
    password = input('Digite sua senha de login: ')
    if verificar_senha(password):
        print("Acesso permitido!")
        return True
