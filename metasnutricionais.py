print("=== METAS NUTRICIONAIS ===")

while True:
    id_metas_nutricionais = input("ID da meta nutricional: ")
    if id_metas_nutricionais != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_criacao = input("Data de criação (AAAA-MM-DD): ")
    if data_criacao != "" and len(data_criacao) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    calorias_diarias = input("Calorias diárias: ")
    if calorias_diarias != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

print("\nMeta nutricional cadastrada!")
