print("=== CADASTRO DE ALIMENTOS ===")

while True:
    alimentos_id = input("ID do alimento: ")
    if alimentos_id != "":
        break
    print("Não pode ficar em branco!")

while True:
    nome = input("Nome do alimento: ")
    if nome != "" and len(nome) <= 100 and nome.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 100 caracteres!")

while True:
    categoria = input("Categoria: ")
    if categoria != "" and len(categoria) <= 255 and categoria.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    calorias = input("Calorias: ")
    if calorias != "":
        break
    print("Não pode ficar em branco!")

while True:
    proteinas = input("Proteínas: ")
    if proteinas != "":
        break
    print("Não pode ficar em branco!")

while True:
    carboidratos = input("Carboidratos: ")
    if carboidratos != "":
        break
    print("Não pode ficar em branco!")

while True:
    gorduras = input("Gorduras: ")
    if gorduras != "" and len(gorduras) <= 255:
        break
    print("Não pode ficar em branco e máximo 255 caracteres!")

while True:
    fibras = input("Fibras: ")
    if fibras != "":
        break
    print("Não pode ficar em branco!")

while True:
    acucares = input("Açúcares: ")
    if acucares != "":
        break
    print("Não pode ficar em branco!")

while True:
    porcao_padrao = input("Porção padrão: ")
    if porcao_padrao != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_inicio = input("Data início (AAAA-MM-DD): ")
    if data_inicio != "" and len(data_inicio) == 10:
        break
    print("Digite exatamente 10 caracteres!")

print("\nAlimento cadastrado!")
