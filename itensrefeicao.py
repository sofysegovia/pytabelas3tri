print("=== ITENS DA REFEIÇÃO ===")

while True:
    id_refeicoes_itens = input("ID do item: ")
    if id_refeicoes_itens != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_refeicoes = input("ID da refeição: ")
    if id_refeicoes != "":
        break
    print("Não pode ficar em branco!")

while True:
    quantidade = input("Quantidade: ")
    if quantidade != "":
        break
    print("Não pode ficar em branco!")

while True:
    calorias_calculada = input("Calorias calculadas: ")
    if calorias_calculada != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_inicio = input("Data início (AAAA-MM-DD): ")
    if data_inicio != "" and len(data_inicio) == 10:
        break
    print("Digite exatamente 10 caracteres!")

print("\nItem adicionado!")
