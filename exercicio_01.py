import json

def leitura_do_arquivo():
    with open('zoologico.json', 'r') as file:
        dados = json.load(file)
    return dados


# agrupar todos animais por cuidador organizando os funcionarios por ordem de idade
# e os nomes dos animais por ordem alfabetica.
#exemplo:

exemplo_organizar_ = [
    {
        "pessoa": {
            "id": 1,
            "nome": "Alice Johnson",
            "cargo": "Gerente",
            "idade": 29,
            "genero": "Feminino",
            "gerente": None,
        },
        "animais": [
             {
                "id": 2,
                "nome": "Leão",
                "idade": 7,
                "genero": "Macho",
                "cuidador": 1,
            },
            {
                "id": 1,
                "nome": "Tigre",
                "idade": 5,
                "genero": "Macho",
                "cuidador": 1,
            },
        ],
    },
    {
        "pessoa": {
            "id": 2,
            "nome": "Bob Brown",
            "cargo": "Cuidador",
            "idade": 40,
            "genero": "Masculino",
            "gerente": 1,
        },
        "animais": [
            {
                "id": 3,
                "nome": "Elefante",
                "idade": 10,
                "genero": "Macho",
                "cuidador": 2,
            },
            {
                "id": 4,
                "nome": "Girafa",
                "idade": 8,
                "genero": "Femea",
                "cuidador": 2,
            },
        ],
    }
]

def organizar_funcionarios_por_ordem_de_idade_e_animais_por_ordem_alfabetica():
    pass