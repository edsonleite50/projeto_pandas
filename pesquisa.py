import sqlite3
import pandas as pd

con = sqlite3.conect('agenda.db')

cur = con.cursor()

resultado = cur.execute("select * from CONTATO")

lista = []


lista = pd.DataFrame()
for linha in resultado.fetchall():
    print(linha[0])
    print(type(linha))
    nomes.append(linha[0])
    enderecos.append(linha[1])
    
print(pd.Series(lista))
