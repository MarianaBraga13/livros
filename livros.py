# Versão 1 apenas do terminal

from db import conectar

lista = []
resposta = input("Selecione abaixo as opções do que gostaria de fazer:\n1- Adicionar um livro\n2- Atualizar um livro\n3- Deletar um livro\nResposta:")
def escolha():
    if resposta =="1":
        inserir_livros(lista)
    elif resposta == "2":
        livros_update()    
    else:
        livros_delete()                

def inserir_livros(lista):
    nome = input("Escreva abaixo o nome do seu livro preferido:\nNome do livro:")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (nome) VALUES (?)', (nome,))
    conn.commit()
    conn.close()
    print("Livro cadastrado com Sucesso!")
    resposta = input("\nDeseja continuar? S ou N ?").strip().upper()    
    if resposta == "S":
        return inserir_livros(lista)
    else:
        return carregar_livros(lista)

    # ler todos os livros cadastrados
def carregar_livros(lista):
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    cadastrados = cursor.fetchall()
    if cadastrados:
        print(f"Seguem os livros cadastrados até o momento:\n")
        for livro in cadastrados:
            lista.append(f"{livro[0]} - {livro[1]}")            
            print(livro)

# deletando a lista
def livros_delete():
    livro_delete = input("Insira o ID do livro que gostaria de deletar:\n").strip() 
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM livros WHERE id=?', (livro_delete,))
        encontrado = cursor.fetchone()
        if encontrado:
            cursor.execute('DELETE FROM livros WHERE id=?', (livro_delete,))
            conn.commit()           
            print("Livro deletado com sucesso!")
        else:
            print("Livro não existe, favor tentar outro id.")
    except Exception as e:
        print(f"Não foi possível deletar porque:{e}")

    finally:
        conn.close()
    carregar_livros(lista)

# update

def livros_update():
    nome_atual = input("Digite o nome do livro que gostaria de atualizar:\n")
    nome_update = input("Digite o novo nome:\n")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE nome=?',(nome_atual,))
    encontrado = cursor.fetchone()
    if encontrado:
        cursor.execute('UPDATE livros SET nome=? WHERE nome=?',(nome_update, nome_atual))
        cursor.commit()
        cursor.close()
        print("Livro atualizado com sucesso!")
    else:
        print("Esse livro não existe, por favor tente novamente.")    

    carregar_livros(lista)
    

