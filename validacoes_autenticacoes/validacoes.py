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
        tipo = input("[1]CPF-[2]RG-[3]CNH ")
        numero = input("Nº do documento: ").strip().replace(
            ".", "").replace("-", "").replace(" ", "")
        if tipo == "1":
            if numero.isdigit() and len(numero) == 11:
                return numero
            else:
                print("Erro: CPF deve conter 11 dígitos.")
        elif tipo == "2":
            if numero.isdigit() and 7 <= len(numero) == 9:
                return numero
            else:
                print("Erro: RG deve conter entre 7 e 9 dígitos.")
        elif tipo == "3":
            if numero.isdigit() and len(numero) == 11:
                return numero
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

# função para informar o modelo de direção do veiculo


def solicitar_direcao():
    while True:
        print("\nInforme a direção do veículo:")
        print("[1] Manual")
        print("[2] Hidráulica")
        print("[3] Semi-hidráulica")

        opcao = input("Escolha uma opção (1/2/3): ").strip()

        if opcao == "1":
            return "Manual"
        elif opcao == "2":
            return "Hidráulica"
        elif opcao == "3":
            return "Semi-hidráulica"
        else:
            print("Opção inválida. Tente novamente.")

# funçãp para informar a situação dos pneus


def informe_pneus():
    print("informe a situação dos pneus [1]Bom [2]Ruim [3]Meia-vida")
    opcao = input("Escolha uma opção ( 1/ 2 / 3 )")
    if opcao == '1':
        return "Bom"
    elif opcao == '2':
        return "Ruim"
    elif opcao == '3':
        return "Meia-vida"
    else:
        print("Opção inválida, tente novamente.")

# função para o tipo de combustivel


def tipo_combustivel():
    print("\n Informe o tipo de combutível ")
    print("[1] Álcool [2] Gásolina [3] Fléx")
    opcao = input("Escolha uma opção ( 1/ 2 / 3 )")

    if opcao == '1':
        return "Álcool"
    elif opcao == '2':
        return "Gasolina"
    elif opcao == '3':
        return "Fléx"
    else:
        print("Opção inválida, tente novamente.")

# função para a opção de genero


def genero():
    opcao = input("Qual o genêro: [M]asculino [F]emino ".strip().lower())
    if opcao == 'm':
        return "masculino"
    elif opcao == "f":
        return "feminino"
    else:
        outro = input("Descreva: ").strip()
        return outro


# função que vai validar o pagamento conforme a forma que for selecionada
