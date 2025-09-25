print("=== EXERCÍCIO FÍSICO ===")

while True:
    id_exercicio_fisico = input("ID do exercício: ")
    if id_exercicio_fisico != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    tipo_exercicio = input("Tipo de exercício: ")
    if tipo_exercicio != "" and len(tipo_exercicio) <= 255 and tipo_exercicio.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    calorias_gastas = input("Calorias gastas: ")
    if calorias_gastas != "":
        break
    print("Não pode ficar em branco!")

while True:
    tempo_exercicio = input("Tempo do exercício (HH:MM): ")
    if tempo_exercicio != "" and len(tempo_exercicio) == 5:
        break
    print("Digite exatamente 5 caracteres!")

print("\nExercício registrado!")
