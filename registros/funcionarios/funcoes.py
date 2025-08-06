import mysql.connector

# função que vai resgistar todos os dados obitidos dos funcionarios no banco de dados


def cadastrarf(con, nome, sobrenome, idade, sexo,
               n_documeto, nome_rua, n_residencia, bairro, cidade, estado,
               pais, telefone, telefone_recado, email, data_cadastro, situacao):

    try:

        cursor = con.cursor()  # conectando ao banco
        # lista para enviar as querys ao banco
        dados = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "sexo": sexo,
            "n_documeto": n_documeto,
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
        query_funcionarios = f"INSERT INTO usuarios({colunas}) VALUES ({placeholders})"

        cursor.execute(query_funcionarios, valores)
        con.commit()

        print("Usuário cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar usuário! {erro}")
    finally:
        cursor.close()


def solicitarDadosF(conexao):
    print("----- CADASTRO DE FUNCIONÁRIO -----")
    nome = input("nome: ")
    sobrenome = input("Sobrenome: ")
    idade = validar_idade()
    sexo = input("Gênero: ")
    _, n_documento = validar_documento()
    nome_rua = input("Qual o nome da rua: ")
    n_residencia = input("Nº da residência: ")
    bairro = input("Nome do bairro: ")
    cidade = input("Cidade que reside:")
    estado = input("Qual estado: ")
    pais = input("Qual pais: ")
    telefone = validar_telefone("Telefone para contato: ")
    telefone_recado = validar_telefone("Telefone para recado: ")
    email = validar_email()
    data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    situacao = "ativo"
    return nome, sobrenome, idade, sexo, n_documento, nome_rua, n_residencia, bairro, cidade, estado, pais, telefone, telefone_recado, email, data_cadastro, situacao
