numero = int(input("Digite um número para calcular a sua fatorial"))
fatorial = 1 
for x in range(numero):
    fatorial = fatorial * (x + 1)

def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None

print(resultado(1))

#Solução do professor