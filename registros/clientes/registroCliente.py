from datetime import datetime
from banco.conexao import banco, closeBanco
from registros.clientes.cliente import cadastrar
from validacoes_autenticacoes.validacoes import (
    validar_documento, validar_email, validar_idade, validar_telefone)

# função que vai ser chamada no "main.py" para solicitar os dados dos clientes


def solicitarDadosC():

    nome = input("nome: ")
    sobrenome = input("Sobrenome: ")
    idade = validar_idade()
    sexo = input("Gênero: ")
    tipoDocumento, n_documento = validar_documento()
    nome_rua = input("Qual o nome da rua: ")
    n_residencia = input("Nº da residência: ")
    bairro = input("Nome do bairro: ")
    cidade = input("Cidade que reside:")
    estado = input("Qual estado: ")
    pais = input("Qual pais: ")
    telefone = validar_telefone("Telefone para contato: ")
    telefone_recado = validar_telefone("Telefone para recado: ")
    email = validar_email()
    data_cadastro = datetime.now(). strftime('%Y-%m-%d %H:%M:%S')
    situacao = "ativo"

    dados = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "sexo": sexo,
        "n_documento": n_documento,
        "nome_rua": nome_rua,
        "n_residencia": n_residencia,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
        "telefone": telefone,
        "telefone_recado": telefone_recado,
        "email": email,
        "data_cadastro": data_cadastro,
        "situacao": situacao
    }

    con = banco()
    cadastrar(con, **dados)
    closeBanco(con)
