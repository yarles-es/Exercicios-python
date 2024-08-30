import json

def leitura_do_arquivo():
    with open('zoologico.json', 'r') as file:
        dados = json.load(file)
    return dados

# separar os animais em grupos de femeas e machos para cada tratador responsavel:
# usar o id do tratador para separar os animais

exemplo = {
    1: {
        'femeas': [
            {
                "id": 1,
                "nome": "Leão",
                "idade": 5,
                "genero": "Masculino",
                "cuidador": 4
            },
            {
                "id": 2,
                "nome": "Tigre",
                "idade": 4,
                "genero": "Feminino",
                "cuidador": 5
            },
        ],
        'machos': [
            {
                "id": 3,
                "nome": "Girafa",
                "idade": 3,
                "genero": "Feminino",
                "cuidador": 4
            },
            {
                "id": 4,
                "nome": "Elefante",
                "idade": 2,
                "genero": "Masculino",
                "cuidador": 5
            },
        ],
    },
    2: {
        'femeas': [
            {
                "id": 5,
                "nome": "Leão",
                "idade": 5,
                "genero": "Masculino",
                "cuidador": 4
            },
            {
                "id": 6,
                "nome": "Tigre",
                "idade": 4,
                "genero": "Feminino",
                "cuidador": 5
            },
        ],
        'machos': [
            {
                "id": 7,
                "nome": "Girafa",
                "idade": 3,
                "genero": "Feminino",
                "cuidador": 4
            },
            {
                "id": 8,
                "nome": "Elefante",
                "idade": 2,
                "genero": "Masculino",
                "cuidador": 5
            },
        ],
    },
}

def separar_grupos_dos_animais_femeas_e_machos_para_cada_tratador_responsavel():
    pass

# apos a resolução do exercicio acima, use a função resolvida para criar uma nova função
# que retorne o nome do tratador e seus respectivos animais femeas e machos

exemplo2 = {
    "nome_tratador": "João",
    "machos": [
        {
            "id": 1,
            "nome": "Leão",
            "idade": 5,
            "genero": "Masculino",
            "cuidador": 4
        },
        {
            "id": 2,
            "nome": "Tigre",
            "idade": 4,
            "genero": "Feminino",
            "cuidador": 5
        },
    ],
    "femeas": [
        {
            "id": 3,
            "nome": "Girafa",
            "idade": 3,
            "genero": "Feminino",
            "cuidador": 4
        },
        {
            "id": 4,
            "nome": "Elefante",
            "idade": 2,
            "genero": "Masculino",
            "cuidador": 5
        },
    ],
}

def retornar_nome_do_tratador_e_seus_respectivos_animais_femeas_e_machos(id_tratador):
    dados = separar_grupos_dos_animais_femeas_e_machos_para_cada_tratador_responsavel()
    # implemente apartir daqui
    pass


# apos a resolução do exercicio acima, use a função e retorne o nome do tratador e apenas os nomes dos respectivos animais machos 
# e um contador que informe quantos animais esse tratador está cuidando,organizando os animais em ordem alfabetica:

exemplo3 = {
    "nome_tratador": "João",
    "machos": [
        "Leão",
        "Tigre",
    ],
    "femeas": [
        "Elefante",
        "Girafa",
    ],
    "total_animais": 4,
}

def retornar_nome_do_tratador_e_seus_respectivos_animais_machos_e_contador_de_animais(id_tratador):
    dados = retornar_nome_do_tratador_e_seus_respectivos_animais_femeas_e_machos(id_tratador)
    # implemente apartir daqui
    pass