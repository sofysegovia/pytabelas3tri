print("=== INGREDIENTES DA RECEITA ===")

while True:
    id_receita_ingrediente = input("ID do ingrediente: ")
    if id_receita_ingrediente != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_alimentos = input("ID do alimento: ")
    if id_alimentos != "":
        break
    print("Não pode ficar em branco!")

while True:
    quantidade = input("Quantidade: ")
    if quantidade != "":
        break
    print("Não pode ficar em branco!")

print("\nIngrediente adicionado!")
