# Aplicação de Console - Cadastro de Usuários

# Lista para armazenar os usuários em memória
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    email = input("E-mail: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida. Deve ser um número inteiro.")
        return

    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    print("\n--- Lista de Usuários Cadastrados ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, u in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {u['nome']} | Email: {u['email']} | Idade: {u['idade']}")

# Função para buscar usuário pelo nome
def buscar_usuario():
    print("\n--- Buscar Usuário por Nome ---")
    nome_busca = input("Digite o nome do usuário: ")
    encontrados = [u for u in usuarios if u['nome'].lower() == nome_busca.lower()]

    if encontrados:
        for u in encontrados:
            print(f"Nome: {u['nome']} | Email: {u['email']} | Idade: {u['idade']}")
    else:
        print("Usuário não encontrado.")

# Menu principal da aplicação
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Buscar Usuário")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()
