# Importando SQLite
import sqlite3 as lite
  
# Criando coneccao
con = lite.connect('dados.db')

# Criando tebela de categoria
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Categoria(id INTEGER PRIMARY KEY, nome TEXT)")

# Criando tebela de receita
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMARY KEY, categoria TEXT, adicionando_em DATE, valor DECIMAL)")

# Criando tebela de gasto
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Gastos(id INTEGER PRIMARY KEY, categoria TEXT, retirado_em DATE, valor DECIMAL)")
