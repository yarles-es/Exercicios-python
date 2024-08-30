import json

def leitura_do_arquivo():
    with open('zoologico.json', 'r') as file:
        dados = json.load(file)
    return dados

# organizar os funcionarios em pacotes de gerentes e funcionarios:
"""
exemplo:
{
    'gerentes': [funcionario1, funcionario2],
    'funcionarios': [funcionario3, funcionario4]
}
"""

def organizar_funcionarios_por_funcionarios_e_gerentes():
    pass

