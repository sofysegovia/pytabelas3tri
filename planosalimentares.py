print("=== PLANOS ALIMENTARES ===")

while True:
    id_planos_alimentares = input("ID do plano alimentar: ")
    if id_planos_alimentares != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_usuario = input("ID do usuário: ")
    if id_usuario != "":
        break
    print("Não pode ficar em branco!")

while True:
    nome = input("Nome do plano: ")
    if nome != "" and len(nome) <= 255 and nome.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    descricao = input("Descrição: ")
    if descricao != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_inicio = input("Data de início (AAAA-MM-DD): ")
    if data_inicio != "" and len(data_inicio) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    calorias_diarias = input("Calorias diárias: ")
    if calorias_diarias != "":
        break
    print("Não pode ficar em branco!")

print("\nPlano alimentar registrado!")
