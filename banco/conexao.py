import mysql.connector
from mysql.connector import Error

# função para conectar ao banco de dados MySQL


def banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="apolo160",
            database="lpveiculos"
        )
        if conexao.is_connected():
            print("Conectado ao banco de dados com sucesso!")
            return conexao
    except Error as erro:
        print(f"Erro ao conectar ao banco de dados{erro}")
        return None

# função para encerrar a conexão com o banco de dados MySQL


def closeBanco(con):
    if con and con.is_connected():
        con.close()
        print("Conexão com o banco de dados foi encerrada!")
