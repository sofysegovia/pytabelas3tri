print("=== RESTRIÇÕES ALIMENTARES ===")

while True:
    id_restricoes_alimentos = input("ID da restrição: ")
    if id_restricoes_alimentos != "":
        break
    print("Não pode ficar em branco!")

while True:
    tipo_restricao = input("Tipo de restrição: ")
    if tipo_restricao != "" and len(tipo_restricao) <= 255 and tipo_restricao.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    id_usuarios = input("ID do usuário: ")
    if id_usuarios != "":
        break
    print("Não pode ficar em branco!")

while True:
    observacoes = input("Observações: ")
    if observacoes != "":
        break
    print("Não pode ficar em branco!")

while True:
    data_criacao = input("Data de criação (AAAA-MM-DD): ")
    if data_criacao != "" and len(data_criacao) == 10:
        break
    print("Digite exatamente 10 caracteres!")

while True:
    usuario_id = input("ID do usuário: ")
    if usuario_id != "":
        break
    print("Não pode ficar em branco!")

print("\nRestrição alimentar registrada!")
