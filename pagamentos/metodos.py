import mysql.connector


def cadastro_pagamento(con, id_aluguel, data_pagamento, valor_pix=0.0, valor_cartao=0.0, valor_dinheiro=0.0):
    try:
        cursor = con.cursor()  # conectando ao banco de dados

        dados = {
            "id_aluguel": id_aluguel,
            "valor_pix": valor_pix,
            "valor_cartao": valor_cartao,
            "valor_dinheiro": valor_dinheiro,
            "data_pagamento": data_pagamento
        }
        colunas = ', '.join(dados.keys())
        placeholders = ', '.join(['%s'] * len(dados))
        valores = list(dados.values())
        query = f"INSERT INTO pagamentos({colunas}) VALUES ({placeholders})"

        cursor.execute(query, valores)
        con.commit()

        print("Pagamento registrado com sucesso")
    except mysql.connector.Error as erro:
        print("Erro a registrar pagamento!")
    finally:
        cursor.close()
