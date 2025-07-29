from datetime import datetime
from banco.conexao import banco, closeBanco
from validacoes_autenticacoes.validacoes import validar_pagamento


def opcoes_pagamento(conexao):
    print(5*"-", " PAGAMENTO ", 5*"-")
    formaPagamento = validar_pagamento()
