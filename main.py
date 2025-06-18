from db import criar_tabelas
from livros import inserir_livros
from livros import carregar_livros
from livros import livros_delete
from livros import livros_update
from livros import escolha

lista = []
#inserir_livros(lista)

if __name__ == "__main__":
    criar_tabelas()
    escolha()
    inserir_livros(lista)
    carregar_livros(lista)
    livros_delete()
    livros_update()
    
