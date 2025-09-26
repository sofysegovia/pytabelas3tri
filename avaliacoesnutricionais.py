print("=== AVALIAÇÕES NUTRICIONAIS ===")

while True:
    id_avaliacoes_nutricionais = input("ID da avaliação: ")
    if id_avaliacoes_nutricionais != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_avaliacao = input("Data da avaliação (AAAA-MM-DD HH:MM): ")
    if data_avaliacao != "":
        break
    print("Não pode ficar em branco!")

while True:
    observacoes = input("Observações: ")
    if observacoes != "":
        break
    print("Não pode ficar em branco!")

while True:
    imc = input("IMC: ")
    if imc != "":
        break
    print("Não pode ficar em branco!")

print("\nAvaliação nutricional registrada!")
