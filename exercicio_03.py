import json

def leitura_do_arquivo():
    with open('zoologico.json', 'r') as file:
        dados = json.load(file)
    return dados

# fazer a função retornar todos os funcionarios e subordinados em pacotes hierarquicos
# exemplo de retorno:
exemplo_ = [
    {
        "pessoa": {
            "id": 1,
            "nome": "Alice Johnson",
            "cargo": "Gerente",
            "idade": 29,
            "genero": "Feminino",
            "gerente": None,
        },
        "subordinados": [
            {
                "pessoa": {
                    "id": 2,
                    "nome": "Bob Brown",
                    "cargo": "Cuidador",
                    "idade": 23,
                    "genero": "Masculino",
                    "gerente": 1,
                },
                "subordinados": []
            },
            {
                "pessoa": {
                    "id": 3,
                    "nome": "Charlie Davis",
                    "cargo": "Cuidador",
                    "idade": 26,
                    "genero": "Masculino",
                    "gerente": 1,
                },
                "subordinados": []
            },
        ],
    },
    {
        "pessoa": {
            "id": 4,
            "nome": "Diana Miller",
            "cargo": "Gerente",
            "idade": 35,
            "genero": "Feminino",
            "gerente": None,
        },
        "subordinados": [
            {
                "pessoa": {
                    "id": 5,
                    "nome": "Eve Wilson",
                    "cargo": "Cuidadora",
                    "idade": 31,
                    "genero": "Feminino",
                    "gerente": 4,
                },
                "subordinados": []
            },
            {
                "pessoa": {
                    "id": 6,
                    "nome": "Frank White",
                    "cargo": "Cuidador",
                    "idade": 33,
                    "genero": "Masculino",
                    "gerente": 4,
                },
                "subordinados": []
            },
        ],
    },
]

def organizar_funcionarios_e_subordinados_pacotes_hierarquicos():
    pass
