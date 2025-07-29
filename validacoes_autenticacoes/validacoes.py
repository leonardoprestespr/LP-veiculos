import re

# função que vai validar se a idade é == 18 anos ou  maior


def validar_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 18:
                print("Erro: idade mínima é 18 anos.")
            else:
                return idade
        except ValueError:
            print("Digite uma idade válida.")

# função para validar se o numero de telefone está correto


def validar_telefone(campo):
    while True:
        telefone = input(f"{campo}: ").strip().replace(
            " ", " ").replace("-", "").replace("(", "").replace(")", "")
        if telefone.isdigit() and 10 <= len(telefone) <= 11:
            return telefone
        else:
            print("Erro: telefone inválido. Digite apenas números")

# função para validar o endereço de email esta correto


def validar_email():
    padrao_email = r'^[\w\.-]+@[\w\.-]+.\w+$'
    while True:
        email = input("Email: ")
        if re.match(padrao_email, email):
            return email
        else:
            print("Erro: email inválido.")

# função que vai validar o número do documento de acordo com o tipo do documento inserido no registro


def validar_documento():
    while True:
        tipo = input("[1]CPF-[2]RG-[3]CNH")
        numero = input("Nº do documento: ").strip().replace(
            ".", "").replace("-", "").replace(" ", "")
        if tipo == "1":
            if numero.isdigit() and len(numero) == 11:
                return tipo, numero
            else:
                print("Erro: CPF deve conter 11 dígitos.")
        elif tipo == "2":
            if numero.isdigit() and 7 <= len(numero) == 9:
                return tipo, numero
            else:
                print("Erro: RG deve conter entre 7 e 9 dígitos.")
        elif tipo == "3":
            if numero.isdigit() and len(numero) == 11:
                return tipo, numero
            else:
                print("Erro: CNH deve conter 11 dígitos:")
        else:
            print("Tipo inválido.")

# função que vai validar se o numero do renavam está correto


def validar_renavam():
    numero = input("Nº do documento:  ")
    if numero.isdigit() and len(numero) == 11:
        return numero
    else:
        print("O Renavam deve conter 11 digítos!")

# função que vai validar o pagamento conforme a forma que for selecionada


def validar_pagamento(ValorAluguel):
    while True:
        opcao = input("[1] Pix [2]Débito [3]Crédito [4] Dinheiro")

        if opcao == "1":
            print("Chave pix: 000.000.000-12")
            valorPago = input("informe o valor pago por PIX: ")
            return ("pix", valorPago)
        elif opcao == "2":
            print("Inserir cartao!")
            valorPago = input("Informe o valor pago no débito: ")
            return ("Débito: ", valorPago)
        elif opcao == "3":
            parcela = input("[1] À vista [2] 2x [3] 3x")
            if parcela = =="1":
                valorPago = input("Valor: ")
            elif parcela == "2":
                valorPago = valorAluguel / 2
            elif parcela == "3":
                valorPago = valorAlugel / 3
            else:
                print("Opção inválida")
        elif opcao == "4":
            troco = valorPago - valorAluguel
            print(f"Troco = R${troco}")
