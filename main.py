from db import criar_tabelas
from livros import inserir_livros
from livros import carregar_livros
from livros import livros_delete

lista = []
#inserir_livros(lista)

if __name__ == "__main__":
    criar_tabelas()
    inserir_livros(lista)
    # carregar_livros(lista)
    livros_delete()
    
