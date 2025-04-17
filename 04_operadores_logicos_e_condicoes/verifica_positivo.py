def eh_positivo(numero):
    return numero > 0


def eh_negativo(numero):
    return numero < 0


def test():
    assert eh_positivo(1)
    assert eh_positivo(2)
    assert eh_positivo(10)
    assert not eh_positivo(0)
    assert not eh_positivo(-1)
    assert not eh_positivo(-10)

    assert eh_negativo(-1)
    assert eh_negativo(-2)
    assert eh_negativo(-10)
    assert not eh_negativo(0)
    assert not eh_negativo(1)
    assert not eh_negativo(10)


print(eh_negativo(-10))
print(eh_positivo(20))
print(eh_positivo(-12))
print(eh_negativo(90))
print(eh_positivo(6))
print(eh_negativo(10))
