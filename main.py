from banco.conexao import banco, closeBanco
from registros.inventario.veiculos import cadastrarV, dadosVeiculo
from registros.dados.registraDados import cadastrar
from registros.dados.solicitadados import solicitarDados
from registros.funcionarios.funcoes import cadastrarf
from alugar.aluguel import registrar_aluguel
from validacoes_autenticacoes.validacoes import validar_documento, validar_email, validar_renavam, validar_telefone, validar_idade
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(__file__))


def menu():
    print(5*"-", "LP Veículos", 5*"-")
    print("1 - Cadastro de cliente")
    print("2 - Cadastro de funcionário")
    print("3 - Registrar veículo")
    print("4 - Registrar aluguel")
    print("0 - Sair")

    return input("Escolha uma opção: ")


def main():
    con = banco()
    while True:
        opcao = menu()

        match opcao:
            case "1":
                dados_cliente = solicitarDados(con)
                cadatrar_no_banco = cadastrar(con, *dados_cliente)
            case "2":
                dados_funcionario = solicitarDados(con)
                cadastrar_funcionario = cadastrarf(con, *dados_funcionario)
            case "3":
                dados_veiculo = dadosVeiculo(con)
                cadastrar_veiculo = cadastrarV(con, *dados_veiculo)
            case "4":
                ...
            case "5":
                ...
            case "0":
                ...
            case _:
                ...
    closeBanco(con)


if __name__ == "__main__":
    main()
