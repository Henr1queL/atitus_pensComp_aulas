def real_para_dolar(valor, tx_conversao): 
    return valor / tx_conversao

def test():
    assert real_para_dolar(500, 5.20) == 96.15384615384616
    assert real_para_dolar(500, 1) == 500.0
    assert real_para_dolar(500, 6) == 83.33333333333333
