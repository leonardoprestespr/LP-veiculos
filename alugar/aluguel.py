
from banco.conexao import banco, closeBanco
from pagamentos.registroPagamento import opcoes_pagamento
from main import menu


def verificar_cliente(con, id_cliente):

    cursor = con.cursor()  # Conectando ao banco

    cursor.execute(
        "SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()

    return cliente is not None


def verificar_veiculo(con, id_veiculo):

    cursor = con.cursor()

    cursor.execute(
        "SELECT status FROM veiculos WHERE id_veiculo = %s", (id_veiculo,))
    resultado = cursor.fetchone()
    cursor.close()

    return resultado and resultado[0].upper == "DISPONIVEL"


def registrar_aluguel(id_cliente, id_veiculo, data_locacao, data_devolucao, forma_pagamento, valor_aluguel):
    con = banco()

    if not verificar_cliente(con, id_cliente):
        print("Cliente não cadastrado no sistema.")
        closeBanco(con)
        return
    if not verificar_veiculo(con, id_veiculo):
        print("Veículo indisponível.")
        closeBanco(con)
        return

# Registrar aluguel

    try:

        cursor = con.cursor()

        dados = {
            "id_cliente": id_cliente,
            "id_veiculo": id_veiculo,
            "data_locacao": data_locacao,
            "data_devolucao": data_devolucao,
            "forma_pagamento": forma_pagamento,
            "valor_aluguel": valor_aluguel
        }
        colunas = ', '.join(dados.keys())
        placeholders = ', '. join(['%s'] * len(dados))
        valores = list(dados.values())
        query = f"INSERT INTO alugueis ({colunas}) VALUES ({placeholders})"

        cursor.execute(query, valores)
        con.commit()
        id_aluguel = cursor.lastrowid  # pega o ID do aluguel

        print("Aluguel registrado com sucesso!")

        if irPagamento == "1":
            opcoes_pagamento(id_aluguel, valor_aluguel)
        elif irPagamento == "2":
            menu()
        else:
            print("Opção inválida!")

    except mysql.connector.Error as erro:
        print(f"Erro ao registrar aluguel{erro}")
    finally:
        cursor.close()
        closeBanco(con)
