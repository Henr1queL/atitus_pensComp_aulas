senha = 5
tentativas = 0


descubra_a_senha = int(input("Digite a Senha de 1 a 10"))

while descubra_a_senha != senha:
    print("Senha Incorreta!")
    descubra_a_senha = int(input("Digite a senha novamente:"))
    tentativa += 1


print("Senha Correta!")
print(f"Número de Tentativas: {tentativas}")

def test():
    assert descobra_a_senha(5, [5]) == 1
    assert descobra_a_senha(5, [0, 11, 3, 5]) == 2  
    assert descobra_a_senha(5, [1, 2, 3, 4, 5]) == -1
    assert descobra_a_senha(5, [1, 2, 3, 4, 5, 5]) == 5