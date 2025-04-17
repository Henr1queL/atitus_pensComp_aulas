def test():
    altura = int(input("Digite um número ímpar maior ou igual a 3: "))

    if altura < 3 or altura % 2 == 0:
        print("Número inválido. Digite um número ímpar maior ou igual a 3.")
    else:
        meio = altura // 2

        for i in range(meio + 1):
            print(" " * (meio - i) + "*" * (2 * i + 1))

        for i in range(meio - 1, -1, -1):
            print(" " * (meio - i) + "*" * (2 * i + 1))