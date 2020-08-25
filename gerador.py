# Imports
from sqlite_bd.select import select_palavras as sp
from sqlite_bd.select import palavra_na_lista as pl
from random import shuffle,seed,random,randint
import pre_processamento.funcoesAuxiliares as fA

# Path do banco de dados
path = "sqlite_bd/palavras.db"

## Recuperando palavras com as características desejadas
def busca_palavras(canonicidade,tonicidade):
    """Busca palavras com as canonicidade e tonicidade dadas.
        Sintaxe:
            palavras = busca_palavras(canonicidade,tonicidade)
        Descrição:
            Busca palavras com as canonicidade e tonicidade que foram informadas.
        Args:
            canonicidade (string): Se a palavra é ou não canônica.
            tonicidade (string): Se a palavra é proparoxítona, paroxítona ou oxítona
        Retornos:
            palavras (list): Lista de palavras
    """
    # Extrai as palavras
    lista_palavras = sp(canonicidade,tonicidade,path)
    # Inicializa gerador de números randômicos e embaralha a lista de palavras
    seed(version=2)
    shuffle(lista_palavras,random)
    return lista_palavras[:30]

def gerar_silabas(palavras):
    """Gera sílabas para o processo de pseudo-palavras.
        Sintaxe:
            (silabas_canonicas,silabas_nao_canonicas) = gerar_silabas(palavras)
        Descrição:
            Gera sílabas para o processo de formação de pseudo-palavras.
        Args:
            palavras (list): Lista de palavras base desejadas.
        Retornos:
            silabas_canonicas (list): Lista de sílabas canônicas.
            silabas_nao_canonicas (list): Lista de síalbas não-canônicas.
    """
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
    """Verificador da validade de uma pseudo-palavra.
        Sintaxe:
            verificacao = pseudo_palavra_valida(palavras)
        Descrição:
            Verifica se uma pseudo-palavra é ou não válida.
        Args:
            pseudo_palavra (string): Pseudo-palavra desejada.
        Retornos:
            verificacao (bool): True (se a pseudo-palavra é válida), False (se a pseudo-palavra não é válida).
    """
    return fA.verifica_silabas(fA.separa_em_silabas(pseudo_palavra)) and not pl(pseudo_palavra,path) \
        and pseudo_palavra not in pseudo_palavras

def pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada):
    """Aplica o algoritmo de geração de pseudo-palavras para palavras oxítonas
        Sintaxe:
            pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
        Descrição:
            Gera pseudo-palavras oxítonas.
        Args:
            pseudo_palavras (list): Lista de pseudo-palavras.
            n_pseudo (int): Número de pseudo-palavras desejado.
            silabas (list): Sílabas que podem compor a pseudo-palavra.
            i (int): Quantidade de sílabas desejadas.
            palavra_hifenizada (list): Sílabas da palavra base. 
        Retornos:
            None: None
    """
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
    """Aplica o algoritmo de geração de pseudo-palavras para palavras paroxítonas
        Sintaxe:
            pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
        Descrição:
            Gera pseudo-palavras paroxítonas.
        Args:
            pseudo_palavras (list): Lista de pseudo-palavras.
            n_pseudo (int): Número de pseudo-palavras desejado.
            silabas (list): Sílabas que podem compor a pseudo-palavra.
            i (int): Quantidade de sílabas desejadas.
            palavra_hifenizada (list): Sílabas da palavra base. 
        Retornos:
            None: None
    """
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
    """Aplica o algoritmo de geração de pseudo-palavras para palavras proparoxítonas
        Sintaxe:
            pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
        Descrição:
            Gera pseudo-palavras proparoxítonas.
        Args:
            pseudo_palavras (list): Lista de pseudo-palavras.
            n_pseudo (int): Número de pseudo-palavras desejado.
            silabas (list): Sílabas que podem compor a pseudo-palavra.
            i (int): Quantidade de sílabas desejadas.
            palavra_hifenizada (list): Sílabas da palavra base. 
        Retornos:
            None: None
    """
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
    """Retorna pseudo-palavras
        Sintaxe:
            pseudo_palavras = pseudo_palavras_oxitona(pseudo_palavras,n_pseudo,silabas,i,palavra_hifenizada)
        Descrição:
            Retorna pseudo-palavras relacionadas com a palavra base desejada.
        Args:
            palavra (string): Palavra desejada.
            n_pseudo (int): Número de pseudo-palavras desejado.
            silabas (list): Sílabas que podem compor a pseudo-palavra. 
        Retornos:
            pseudo_palavras (list): Lista de pseudo-palavras formadas.
    """
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