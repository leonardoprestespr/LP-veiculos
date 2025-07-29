import mysql.connector
from banco.conexao import banco, closeBanco

# função que vai registrar os dados dos veículos no banco MySQL


def cadastrarV(marca, modelo, cor, qnt_portas, renavam, combustivel, direcao,
               potencia_motor, pneus, obs, valor_veiculo, data_cadastro, situacao):
    try:
        cursor = con.cursor()
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
        colunas = ', '.join(dados.keys())
        placeholders = ', '.join(['%s'] * len(dados))
        valores = list(dados.values())
        query_veiculos = "INSERT INTO veiculos ({colunas}) VALUES ({placeholders})"

        cursor.execute(query, valores)
        con.commit()

        print("Veículo cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao cadastrar veículo")
    finally:
        cursor.close()
