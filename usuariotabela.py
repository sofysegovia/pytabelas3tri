print("=== CADASTRO DE USUÁRIO ===")

id_usuarios = 1
altura = float(input("Digite sua altura (ex: 1.75): "))
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")
peso = float(input("Digite seu peso (ex: 70.5): "))
data_nascimento = input("Digite sua data de nascimento (AAAA-MM-DD): ")


print("\n=== DADOS CADASTRADOS ===")
print("ID:", id_usuarios)
print("Altura:", altura, "m")
print("Nome:", nome)
print("Email:", email)
print("Senha:", senha)
print("Peso:", peso, "kg")
print("Data de Nascimento:", data_nascimento)

print("\nCadastro realizado com sucesso!")
