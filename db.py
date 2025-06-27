import sqlite3

# conexão com banco de dados
def conectar():
    return sqlite3.connect("livros.db")

# criar tabelas
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS livros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   autor TEXT NOT NULL
                   );
            """)
    
    conn.commit()
    conn.close()