# Imports
from sqlite_bd.select import select_palavras as sp
from sqlite_bd.select import palavra_na_lista as pl
from random import shuffle,seed,random,randint
import pre_processamento.funcoesAuxiliares as fA

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

def gerar_silabas(palavras):
    silabas_canonicas = []
    silabas_nao_canonicas = []
    for p in palavras:
        aux_silabas = fA.separa_em_silabas(p)
        for s in aux_silabas:
            if not fA.tem_acento(s)[0]:
                if fA.canonicidade(s):
                     if s not in silabas_canonicas:
                        silabas_canonicas.append(s)
                else:
                    if s not in silabas_nao_canonicas:
                        silabas_nao_canonicas.append(s)
    return silabas_canonicas,silabas_nao_canonicas

def pseudo_palavra_valida(pseudo_palavra,pseudo_palavras):
    return fA.verifica_silabas(fA.separa_em_silabas(pseudo_palavra)) and not pl(pseudo_palavra,path) \
        and pseudo_palavra not in pseudo_palavras

def pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada):
    aux_pseudo_palavras = ''
    while len(pseudo_palavras) < n_pseudo:
        shuffle(silabas,random)
        aux_silabas = silabas[:i]
        for s in aux_silabas:
            for l in s:
                aux_pseudo_palavras += l
        aux_pseudo_palavras += palavra_hifenizada[-1]
        if pseudo_palavra_valida(aux_pseudo_palavras,pseudo_palavras):
            pseudo_palavras.append(aux_pseudo_palavras)
        aux_pseudo_palavras = ''

def pseudo_palavras_paroxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada):
    aux_pseudo_palavras = ''
    while len(pseudo_palavras) < n_pseudo:
        shuffle(silabas,random)
        aux_silabas = silabas[:i]
        for j in range(i-1):
            for l in aux_silabas[j]:
                aux_pseudo_palavras += l
        aux_pseudo_palavras += palavra_hifenizada[-2]
        aux_pseudo_palavras += silabas[-1]
        if pseudo_palavra_valida(aux_pseudo_palavras,pseudo_palavras):
            pseudo_palavras.append(aux_pseudo_palavras)
        aux_pseudo_palavras = ''

def pseudo_palavras_proparoxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada):
    aux_pseudo_palavras = ''
    while len(pseudo_palavras) < n_pseudo:
        shuffle(silabas,random)
        aux_silabas = silabas[:i]
        for j in range(i-2):
            for l in aux_silabas[j]:
                aux_pseudo_palavras += l
        aux_pseudo_palavras += palavra_hifenizada[-3]
        aux_pseudo_palavras += silabas[-1]
        aux_pseudo_palavras += silabas[-2]
        if pseudo_palavra_valida(aux_pseudo_palavras,pseudo_palavras):
            pseudo_palavras.append(aux_pseudo_palavras)
        aux_pseudo_palavras = ''
        
def get_pseudo_palavras(palavra,n_pseudo,silabas):
    pseudo_palavras = []
    palavra_hifenizada = fA.separa_em_silabas(palavra)
    seed(version=2)
    if fA.canonicidade(palavra):
        silabas = silabas[0]
    else:
        silabas = silabas[0] + silabas[1]
    if fA.tonicidade(palavra) == "oxítona":
        i = 2 + randint(0,99) % 3
        pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
    elif fA.tonicidade(palavra) == "paroxítona":
        i = 3 + randint(0,99) % 3
        pseudo_palavras_paroxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
    else:
        i = 5 + randint(0,99) % 3
        pseudo_palavras_proparoxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
    return pseudo_palavras