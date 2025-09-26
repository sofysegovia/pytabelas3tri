print("=== SUPLEMENTAÇÃO DO USUÁRIO ===")

while True:
    id_avaliacoes_nutricionais = input("ID da avaliação nutricional: ")
    if id_avaliacoes_nutricionais != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    nome_suplemento = input("Nome do suplemento: ")
    if nome_suplemento != "" and len(nome_suplemento) <= 255 and nome_suplemento.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    dosagem = input("Dosagem: ")
    if dosagem != "":
        break
    print("Não pode ficar em branco!")

while True:
    frequencia = input("Frequência: ")
    if frequencia != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_inicio = input("Data de início (AAAA-MM-DD): ")
    if data_inicio != "" and len(data_inicio) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    data_fim = input("Data de fim (AAAA-MM-DD): ")
    if data_fim != "" and len(data_fim) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    observacoes = input("Observações: ")
    if observacoes != "":
        break
    print("Não pode ficar em branco!")

print("\nSuplementação registrada!")
