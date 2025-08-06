from datetime import datetime
# from registros.dados.registraDados import cadastrar
from validacoes_autenticacoes.validacoes import (
    validar_documento, validar_email, validar_idade, validar_telefone, genero)

# função que vai ser chamada no "main.py" para solicitar os dados dos clientes


def solicitarDados(banco):
    print("----- CADASTRO -----")
    nome = input("nome: ")
    sobrenome = input("Sobrenome: ")
    idade = validar_idade()
    sexo = genero()
    n_documento = validar_documento()
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
    return nome, sobrenome, idade, sexo, n_documento, nome_rua, n_residencia, bairro, cidade, estado, pais, telefone, telefone_recado, email, data_cadastro, situacao
