# Imports
import sqlite3 as sql

# Linha temporária enquanto fase de testes
import os
os.remove("palavras.db") if os.path.exists("palavras.db") else None

# Criando uma conexão com o banco
con = sql.connect("palavras.db")

# Criando um cursor
cur = con.cursor()

# Criando a tabela palavra
sql_create = 'create table palavra '\
             '(id varchar(20) primary key not null, '\
             'canonicidade int not null, '\
             'tonicidade varchar(14)) not null '

# Executando a query sql_create
cur.execute(sql_create)

# Definindo insert query
sql_insert = 'insert into palavra values (?,?,?)'

with open("../PreProcessamento/palavrasProcessadas.csv",'r') as arq:
    next(arq)
    for line in arq:
        line = line.split(',')
        line[2] = line[2].rstrip()
        cur.execute(sql_insert,(line[0],line[1],line[2]))

# Gravando os dados no banco
con.commit()

# # Verificando registros
# Definindo select query
sql_select = 'select * from palavra'
cur.execute(sql_select)
registros = cur.fetchall()
for reg in registros:
    print('Palavra: %s, Canonicidade: %s, Tonicidade: %s \n' % reg) 

# Fechando a conexão
con.close()       