# Pesquisa de Satisfação - Empresa TudoWeb

# Contadores das respostas
excelente = 0
bom = 0
ruim = 0

# Cadastro de 50 entrevistados
for i in range(1, 51):

    print("\n------------------------------")
    print(f"ENTREVISTADO {i}")
    print("------------------------------")

    # Entrada dos dados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nOPINIÃO SOBRE O ATENDIMENTO")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    # Verificação da opinião
    while opiniao not in [1, 2, 3]:
        print("Opinião inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")

    elif opiniao == 2:
        bom += 1
        print("Opinião registrada: BOM")

    elif opiniao == 3:
        ruim += 1
        print("Opinião registrada: RUIM")

# Resultado final da pesquisa
print("\n==============================")
print("RESULTADO DA PESQUISA - TUDOWEB")
print("==============================")

print(f"Total de respostas EXCELENTE: {excelente}")
print(f"Total de respostas RUIM: {ruim}")
print(f"Total de respostas BOM: {bom}")

print("==============================")
