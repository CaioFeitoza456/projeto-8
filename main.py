
import json

def adiciona_usuario(lista):
    dados = {}

    # Lendo as informações do usuário        
    dados["email"] = input("Digite o email >>> ")
    dados["senha"] = input("Digite a senha >>> ")

    # Salvando as informações do usuário
    lista.append(dados)


def listar_usuarios(caminho_arquivo, lista_de_usuarios):
    
    # Verifica se o arquivo de dados está criado, caso não, entre
    # no except
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            # Envia o arquivo json para a variável 'lista_de_usuarios'
            lista_de_usuarios = json.load(arquivo)
    
    except FileNotFoundError:
        print("Nenhum usuário foi criado ainda.")
        return

    # Pegando o tamanho da lista de usuários criados
    tamanho_lista = len(lista_de_usuarios)

    # Verifica se tem ao menos 1 usuário para listar
    if not tamanho_lista >= 1:
        print("Não há nada para listar.")
        return
    
    # Lista os usuários caso passe da verificação
    print("Os usuários criados foram:")
    for usuario in lista_de_usuarios:
        
        print("~" * 30)
        
        # Imprime todos os usuários da lista
        for chave , valor in usuario.items():
            print(f"{chave} >>> {valor}")
        
        print("~" * 30)


def salvar_dados(caminho_arquivo, dados):
    # Salva os usuários criados em um arquivo .json chamado dados.json
    # (Caso o arquivo não exista, o programa cria um)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2)
        print("Arquivo salvo com sucesso!")


def limpar_lista_de_usuarios(caminho_arquivo):
    verificacao =  input("Você realmete deseja limpar ? (Todos os dados serão excluídos): ")
    verificacao = verificacao.strip().capitalize()

    if verificacao == "Sim":
        # Reescreve no arquivo já existente uma lista vazia
        with open(caminho_arquivo, "w") as arquivo:
            json.dump([], arquivo)
            print("Arquivo limpo com sucesso!")
    
    else:
        print("Digite apenas 'Sim' ou 'Não'.")


# Caso o seu sistema NÃO seja Windows, troque as duas barras invertidas
# por apenas uma normal
caminho_arquivo = "cadastros_de_emails\\dados.json"
lista_usuarios = []

while True:
    print("""
1 - Cadastrar novo usuário
2 - Listar usuários criados
3 - Salvar
4 - Limpar lista de usuários
5 - Encerrar programa
""")
    
    # Leitura da opção escolhida pelo usuário
    opcao = input("Digite aqui: ")

    if opcao == "1":
    
        adiciona_usuario(lista_usuarios)

    elif opcao == "2":

        listar_usuarios(caminho_arquivo, lista_usuarios)

    elif opcao == "3":
        
        salvar_dados(caminho_arquivo, lista_usuarios)
    
    elif opcao == "4":

        limpar_lista_de_usuarios(caminho_arquivo)

    elif opcao == "5":
        print("Tchau!")
        break

