
print('==== CAMINHO DAS ÍNDIAS ====')
# Cardápio
def cardapio():
    print("\n===== CARDÁPIO =====")
    print("1 - Arroz basmatti - R$ 15,00")
    print("2 - Curry de carne - R$ 35,00")
    print("3 - Curry de legumes - R$ 15,00")
    print("4 - Curry de frango - R$ 25,00")
    print("5 - Dhal de lentilhas - R$ 30,00")


# Pedido
def pedido():
    total = 0

    while True:
        try:
            codigo = int(input("\nDigite o código do prato (0 para encerrar): "))

            if codigo == 0:
                break

            elif codigo == 1:
                preco = 15
                prato = "Arroz basmatti"

            elif codigo == 2:
                preco = 35
                prato = "Curry de carne"

            elif codigo == 3:
                preco = 15
                prato = "Curry de legumes"

            elif codigo == 4:
                preco = 25
                prato = "Curry de frango"

            elif codigo == 5:
                preco = 30
                prato = "Dhal de lentilhas"

            else:
                print("Código inexistente!")
                continue

            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("Quantidade inválida!")
                continue

            subtotal = preco * quantidade
            total = total + subtotal

            print(f"{quantidade}x {prato} adicionado(s).")
            print(f"Subtotal: R$ {subtotal:.2f}")

        except ValueError:
            print("Erro! Digite apenas números.")

    return total


# Fechamento
def fechamento(numero, mesa, garcom, total):
    print("\n===== FECHAMENTO =====")
    print(f"Número do pedido: {numero}")
    print(f"Mesa: {mesa}")
    print(f"Garçom: {garcom}")
    print(f"Total da conta: R$ {total:.2f}")


# Programa principal
try:
    numero = int(input("Número do pedido: "))
    mesa = int(input("Número da mesa: "))
    garcom = input("Nome do garçom: ")

    cardapio()

    total = pedido()

    fechamento(numero, mesa, garcom, total)

except ValueError:
    print("Erro! Digite um número válido.")
