def calcular_juros_compostos(principal, taxa, tempo):
    return principal * (1 + taxa) ** tempo


def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if tempo == 0:
        return principal
    return calcular_juros_compostos_recursivo(principal, taxa, tempo - 1) * (1 + taxa) 

def test_calcular_juros_compostos():
    assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442 
    assert calcular_juros_compostos(1000, 0.05, 0) == 1000

def test_calcular_juros_compostos_recursivo():
    assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.8946267774422
    assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000  