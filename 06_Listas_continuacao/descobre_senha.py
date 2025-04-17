def descubra_a_senha(senha, tentativas_lista):
    tentativas = 0
    for tentativa in tentativas_lista:
        if tentativa == senha:
            return tentativas + 1 
        tentativas += 1
    return -1  

senha = 5
tentativas_lista = []

descubra_a_senha_input = int(input("Digite a Senha de 1 a 10: "))

while descubra_a_senha_input != senha:
    print("Senha Incorreta!")
    tentativas_lista.append(descubra_a_senha_input)
    descubra_a_senha_input = int(input("Digite a senha novamente: "))

tentativas_lista.append(descubra_a_senha_input)
print("Senha Correta!")
print(f"Número de Tentativas: {len(tentativas_lista)}")

def test():
    assert descubra_a_senha(5, [5]) == 1
    assert descubra_a_senha(5, [0, 11, 3, 5]) == 2  
    assert descubra_a_senha(5, [1, 2, 3, 4, 5]) == -1
    assert descubra_a_senha(5, [1, 2, 3, 4, 5, 5]) == 5
