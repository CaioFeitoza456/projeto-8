"""
Sistema de cadastro de contas de um
serviço qualquer. O usuário deve 
fornecer um email e senha. Os dados
devem ser guardados em um arquivo
.json.
"""

import json


caminho_arquivo = "dados_usuarios.json"


dados_usuario = {
    "usuario": None,
    "email": None,
    "senha": None,
}


while True:
    usuario = input("Digite o nome de usuário: ")
    tamanho_usuario = len(usuario)

    if not tamanho_usuario < 3:
        dados_usuario["usuario"] = usuario
        break
    
    print("Nome muito curto, tente outro")


while True:
    email = input("Digite o email: ")
    
    if not "@" in email:
        print("Digite um email válido.")
        continue
    
    dados_usuario["email"] = email
    break


while True:
    senha = input("Digite a senha: ")
    tamanho_senha = len(senha)
    
    if tamanho_senha < 5:
        print("A senha é muito curta, tente outra.")
        continue
    
    dados_usuario["senha"] = senha
    break


with open(caminho_arquivo, "a", encoding="utf8") as arquivo:
    json.dump(
        dados_usuario, 
        arquivo, 
        indent=2
    )
    print("Dados cadastrados com sucesso!")
