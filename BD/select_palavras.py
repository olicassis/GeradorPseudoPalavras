# Imports
import sqlite3 as sql

def select_palavras(canonicidade,tonicidade):
    lista_palavras = []
    sql_select = "select id from palavra where canonicidade = '{}' and tonicidade = '{}'".format(canonicidade,tonicidade)
    print(sql_select)
    # Conectando ao banco de dados
    con = sql.connect('palavras.db')
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