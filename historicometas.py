print("=== HISTÓRICO DE METAS ===")

while True:
    id_historico_metas = input("ID do histórico: ")
    if id_historico_metas != "":
        break
    print("Não pode ficar em branco!")

while True:
    tipos_meta = input("Tipo de meta: ")
    if tipos_meta != "" and len(tipos_meta) <= 50 and tipos_meta.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 50 caracteres!")

while True:
    nome = input("Nome da meta: ")
    if nome != "" and len(nome) <= 255 and nome.replace(" ", "").isalpha():
        break
    print("Digite apenas letras e máximo 255 caracteres!")

while True:
    descricao = input("Descrição: ")
    if descricao != "":
        break
    print("Não pode ficar em branco!")

while True:
    valor_anterior = input("Valor anterior: ")
    if valor_anterior != "":
        break
    print("Não pode ficar em branco!")

while True:
    valor_novo = input("Valor novo: ")
    if valor_novo != "":
        break
    print("Não pode ficar em branco!")

while True:
    id_metas_nutricionais = input("ID da meta nutricional: ")
    if id_metas_nutricionais != "":
        break
    print("Não pode ficar em branco!")

print("\nHistórico registrado!")
