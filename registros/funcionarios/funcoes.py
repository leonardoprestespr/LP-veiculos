import mysql.connector

# função que vai resgistar todos os dados obitidos dos funcionarios no banco de dados


def cadastrar(con, nome, sobrenome, idade, sexo,
              n_documento, nome_rua, n_residencia, bairro, cidade, estado,
              pais, telefone, telefone_recado, email, data_cadastro, situacao):

    try:

        cursor = con.cursor()  # conectando ao banco
        # lista para enviar as querys ao banco
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
        colunas = ', '.join(dados.keys())
        placeholders = ', '.join(['%s'] * len(dados))
        valores = list(dados.values())
        query = f"INSERT INTO usuarios({colunas}) VALUES ({placeholders})"

        cursor.execute(query, valores)
        con.commit()

        print("Usuário cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar usuário! {erro}")
    finally:
        cursor.close()
