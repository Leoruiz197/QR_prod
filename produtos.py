import json
import os

CAMINHO_ARQUIVO = 'dados.json'

def ler_produtos():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_produtos(produtos):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def adicionar_produto(nome, quantidade=1):
    produtos = ler_produtos()
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            produto['quantidade'] += quantidade
            salvar_produtos(produtos)
            return
    produtos.append({'nome': nome, 'quantidade': quantidade})
    salvar_produtos(produtos)
