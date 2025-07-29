from registros.clientes.registroCliente import solicitarDadosC
from registros.funcionarios.registroFuncionario import solicitarDadosF
from registros.inventario.registroVeiculo import dadosVeiculo
from alugar.aluguel import registrar_aluguel
import sys
import os

sys.path.append(os.path.dirname(__file__))


def menu():
    while True:
        print(5*"-", "MENU PRINCIPAL", 5*"-")
        print("1 - Cadastro de cliente")
        print("2 - Cadastro de funcionário")
        print("3 - Registrar veículo")
        print("4 - Registrar aluguel")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            solicitarDadosC()
        elif opcao == "2":
            solicitarDadosF()
        elif opcao == "3":
            dadosVeiculo()
        elif opcao == "4":
            registrar_aluguel()
        elif opcao == "0":
            print("Encerrando....")
        else:
            print("Opção Inválida, tente novamente.")


if __name__ == "__main__":
    menu()
