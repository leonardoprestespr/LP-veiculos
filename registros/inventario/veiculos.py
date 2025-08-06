import mysql.connector
from datetime import datetime
from banco.conexao import banco, closeBanco
from validacoes_autenticacoes.validacoes import validar_renavam, solicitar_direcao, informe_pneus, tipo_combustivel

# função que vai registrar os dados dos veículos no banco MySQL


def cadastrarV(con, marca, modelo, cor, qnt_portas, renavam, combustivel, direcao,
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
        query_veiculos = f"INSERT INTO veiculos ({colunas}) VALUES ({placeholders})"

        cursor.execute(query_veiculos, valores)
        con.commit()

        print("Veículo cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao cadastrar veículo")
    finally:
        cursor.close()


def dadosVeiculo(conexao):
    marca = input("Qual a marca:")
    modelo = input("Qual o modelo: ")
    cor = input("Cor: ")
    qnt_portas = int(input("Quantidade de portas: "))
    renavam = validar_renavam()
    combustivel = tipo_combustivel()
    direcao = solicitar_direcao()
    potencia_motor = input("Informe a potência do motor: ")
    pneus = informe_pneus()
    obs = input("Informe as condições do veiculo: ")
    valor_veiculo = input("Informe o valor do veiculo: ",)
    data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    situacao = "DISPONIVEL"
    return marca, modelo, cor, qnt_portas, renavam, combustivel, direcao, potencia_motor, pneus, obs, valor_veiculo, data_cadastro, situacao
