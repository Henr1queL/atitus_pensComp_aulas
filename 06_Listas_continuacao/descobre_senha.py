def qual_senha(senha, tentativas_totais):
    tentativas_totais = 0
    for tentativa in tentativas_totais:
        if tentativa < 1 or tentativa > 10:
            continue
        tentativas_totais += 1
        if tentativa == senha:
            return tentativas_totais
    return -1  

def test():
    assert qual_senha(6, [6]) == 1
    assert qual_senha(6, [0, 11, 3, 6]) == 2  
    assert qual_senha(6, [1, 2, 3, 4, 5]) == -1
    assert qual_senha(6, [1, 2, 3, 4, 5, 6]) == 6