import json
import os
from models.conta import Conta
from models.conta_corrente import ContaCorrente

CAMINHO_ARQUIVO = "../data/contas.json"

class BancoDados:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(CAMINHO_ARQUIVO):
            with open