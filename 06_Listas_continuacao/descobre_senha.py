senha =  5
tentativas = 1
descubra_a_senha = int(input("Digite a Senha de 1 a 10"))

while descubra_a_senha != senha:
    print("Senha Incorreta!")
    descubra_a_senh = int(input("Digite a senha novamente:"))
    tentativa += 1

def test():
    print("Senha Correta!")
    print("Número de Tentativas:", tentativas)