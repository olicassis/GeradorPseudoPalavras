# Imports
from sqlite_bd.select import select_palavras as sp
from random import shuffle,seed,random

# Path do banco de dados
path = "sqlite_bd/palavras.db"

## Recuperando palavras com as características desejadas
def busca_palavras(canonicidade,tonicidade):
    # Extrai as palavras
    lista_palavras = sp(canonicidade,tonicidade,path)
    # Inicializa gerador de números randômicos e embaralha a lista de palavras
    seed(version=2)
    shuffle(lista_palavras,random)
    return lista_palavras[:30]

#def get_pseudo_palavras(shuffled_list, palavras):