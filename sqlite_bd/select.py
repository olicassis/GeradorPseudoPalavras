# Imports
import sqlite3 as sql

def select_palavras(canonicidade,tonicidade,path):
    lista_palavras = []
    sql_select = "select id from palavra where canonicidade = '{}' and tonicidade = '{}'".format(canonicidade,tonicidade)
    # Conectando ao banco de dados
    con = sql.connect(path)
    # Cursor
    cur = con.cursor()
    # Executando a query
    cur.execute(sql_select)
    palavras = cur.fetchall()
    # Recuperando as palavras
    for p in palavras:
        lista_palavras.append(p[0])
    # Fechando a conexão com o banco
    con.close()
    # Retorna as palavras encontradas
    return lista_palavras

def palavra_na_lista(palavra,path):
    sql_select = 'select id from palavra where id = "{}"'.format(palavra)
    # Conectando ao banco de dados
    con = sql.connect(path)
    # Cursor
    cur = con.cursor()
    # Executanado a query
    cur.execute(sql_select)
    palavra = cur.fetchall()
    # Fechando a conexão com o banco
    con.close()
    return True if palavra != [] else False