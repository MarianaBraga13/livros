from db import criar_tabelas
from livros import inserir_livros, carregar_livros, livros_delete, livros_update

def menu():
    criar_tabelas()
    lista = []
    
    while True:
        resposta = input(
            "\n============= 📚 Biblioteca Py ===========\n"
            "1 - Adicionar um livro\n" 
            "2 - Atualizar um livro\n" 
            "3 - Deletar um livro\n" 
            "4 - Ver todos os livros\n" 
            "0 - Sair\n" 
            "\nEscolha uma opção: \n").strip()

        if resposta == "1":
            inserir_livros()

        elif resposta == "2":
            livros_update()

        elif resposta == "3":
            livros_delete()

        elif resposta == "4":
            carregar_livros(lista)

        elif resposta == "0":
            break            
    
        else:
            print("Digite o número de escolha apenas das opções.")

if __name__ == "__main__":
    menu()


