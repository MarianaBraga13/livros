# Versão 1 apenas do terminal

from db import conectar
lista = []

def inserir_livros():
    nome = input("Escreva abaixo o nome do seu livro preferido:\nNome do livro:").strip()
    autor = input("Escreva agora o nome do autor(a):").strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (nome , autor) VALUES (? , ?)', (nome, autor))
    conn.commit()
    conn.close()
    print("Livro cadastrado com Sucesso!")

    # ler todos os livros cadastrados
def carregar_livros(lista):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    cadastrados = cursor.fetchall()
    if cadastrados:
        print("\n============= Biblioteca Py ===========\n")
        print("Seguem os livros cadastrados até o momento:\n")
        for livro in cadastrados:
            lista.append(f"{livro[0]} - {livro[1]}")            
            print(livro)

    else:
        print("Ainda não há nenhum livro cadastrado.")
    conn.close()        

# deletando a lista
def livros_delete():
    carregar_livros([])
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

# update

def livros_update():
    carregar_livros([])
    id = int(input("\nDigite o código ID do livro que gostaria de atualizar:\n").strip())
    nome_update = input("Digite o novo nome:\n").strip()
    autor_update = input("Confirme o nome do autor:\n").strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE livros SET nome=?, autor=? WHERE id=?',
    (nome_update , autor_update , id))
    if cursor.rowcount > 0:
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.") 
    conn.commit()
    conn.close()       
   