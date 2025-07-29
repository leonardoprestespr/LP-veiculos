from datetime import datetime
from banco.conexao import banco, closeBanco
from registros.inventario.veiculos import cadastrarV
from validacoes_autenticacoes.validacoes import (
    validar_documento, validar_email, validar_idade, validar_telefone)

# função que vai ser chamada no "main.py" para solicitar dados do veiculo ao registrar no inventario


def dadosVeiculo():
    marca = input("Qual a marca:")
    modelo = input("Qual o modelo: ")
    cor = input("Cor: ")
    qnt_portas = int(input("Quantidade de portas: "))

    dados = {
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "qnt_portas": qnt_portas,
        "renavam": renavam,
        "combustivel": combustivel,
        "direcao": direcao,
        "potencia_motor": potencia_motor,
        "pneus": pneus,
        "obs": obs,
        "valor_veiculo": valor_veiculo,
        "data_cadastro": data_cadastro,
        "situacao": situacao
    }
