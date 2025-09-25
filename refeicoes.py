print("=== CADASTRO DE REFEIÇÕES ===")

while True:
    refeicoes_id = input("ID da refeição: ")
    if refeicoes_id != "" and len(refeicoes_id) <= 100:
        break
    print("Não pode ficar em branco e máximo 100 caracteres!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    tipo_refeicao = input("Tipo de refeição: ")
    if tipo_refeicao != "" and len(tipo_refeicao) <= 255 and tipo_refeicao.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    data_refeicao = input("Data da refeição (AAAA-MM-DD): ")
    if data_refeicao != "" and len(data_refeicao) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    horario = input("Horário (HH:MM): ")
    if horario != "" and len(horario) == 5:
        break
    print("Digite exatamente 5 caracteres!")

while True:
    total_calorias = input("Total de calorias: ")
    if total_calorias != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_proteinas = input("Total de proteínas: ")
    if total_proteinas != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_carboidratos = input("Total de carboidratos: ")
    if total_carboidratos != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_gorduras = input("Total de gorduras: ")
    if total_gorduras != "":
        break
    print("Não pode ficar em branco!")

while True:
    observacoes = input("Observações: ")
    if observacoes != "":
        break
    print("Não pode ficar em branco!")

print("\nRefeição cadastrada!")print("=== CADASTRO DE REFEIÇÕES ===")

while True:
    refeicoes_id = input("ID da refeição: ")
    if refeicoes_id != "" and len(refeicoes_id) <= 100:
        break
    print("Não pode ficar em branco e máximo 100 caracteres!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    tipo_refeicao = input("Tipo de refeição: ")
    if tipo_refeicao != "" and len(tipo_refeicao) <= 255 and tipo_refeicao.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    data_refeicao = input("Data da refeição (AAAA-MM-DD): ")
    if data_refeicao != "" and len(data_refeicao) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    horario = input("Horário (HH:MM): ")
    if horario != "" and len(horario) == 5:
        break
    print("Digite exatamente 5 caracteres!")

while True:
    total_calorias = input("Total de calorias: ")
    if total_calorias != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_proteinas = input("Total de proteínas: ")
    if total_proteinas != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_carboidratos = input("Total de carboidratos: ")
    if total_carboidratos != "":
        break
    print("Não pode ficar em branco!")

while True:
    total_gorduras = input("Total de gorduras: ")
    if total_gorduras != "":
        break
    print("Não pode ficar em branco!")

while True:
    observacoes = input("Observações: ")
    if observacoes != "":
        break
    print("Não pode ficar em branco!")

print("\nRefeição cadastrada!")
