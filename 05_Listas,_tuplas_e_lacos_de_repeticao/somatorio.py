def somatorio(numero):
    if numero < 0:
        return  None
    resultado = 0
    for n in range(numero + 1):
        resultado += n
        print(n, resultado)
    return resultado
>>>>>>> 0a60f9ab8440234212178cc4bdf5d82a8d53530b

<<<<<<< HEAD
while resultado in range(10):
    print(total, resultado)
return resultado



def test():
    assert somatorio(-1) is None
    assert somatorio(0) == 0
    assert somatorio(1) == 1
    assert somatorio(2) == 3
    assert somatorio(3) == 6
    assert somatorio(4) == 10
    assert somatorio(5) == 15
    assert somatorio(6) == 21
    assert somatorio(7) == 28
    assert somatorio(8) == 36
    assert somatorio(9) == 45
=======
def test():
    assert somatorio(-1) is None
    assert somatorio(0) == 0
    assert somatorio(1) == 1
    assert somatorio(2) == 3
    assert somatorio(3) == 6
    assert somatorio(4) == 10
    assert somatorio(5) == 15
    assert somatorio(6) == 21
    assert somatorio(7) == 28
    assert somatorio(8) == 36
    assert somatorio(9) == 45

print(somatorio(1))
>>>>>>> 0a60f9ab8440234212178cc4bdf5d82a8d53530b