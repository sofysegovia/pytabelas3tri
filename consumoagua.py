print("=== CONSUMO DE ÁGUA ===")

while True:
    id_consumo_agua = input("ID do consumo: ")
    if id_consumo_agua != "":
        break
    print("Não pode ficar em branco!")

while True:
    quantidade_ml = input("Quantidade em mL: ")
    if quantidade_ml != "":
        break
    print("Não pode ficar em branco!")

while True:
    meta_diaria_ml = input("Meta diária em mL: ")
    if meta_diaria_ml != "" and len(meta_diaria_ml) <= 255:
        break
    print("Não pode ficar em branco e máximo 255 caracteres!")

while True:
    data_criacao = input("Data de criação (AAAA-MM-DD): ")
    if data_criacao != "" and len(data_criacao) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    id_metas_nutricionais = input("ID da meta nutricional: ")
    if id_metas_nutricionais != "" and len(id_metas_nutricionais) <= 100:
        break
    print("Não pode ficar em branco e máximo 100 caracteres!")

print("\nConsumo de água registrado!")
