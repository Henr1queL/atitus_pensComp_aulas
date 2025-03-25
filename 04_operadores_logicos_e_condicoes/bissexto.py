def eh_bissexto(ano):
    if ano % 4 == 0:
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)  


def proximo_bissexto(ano):
    ano += 1
    if ano % 400 == 0:
        return ano
    elif ano % 100 == 0:
        return + 4
    elif ano % 4 == 0:
        return ano
    else:
        return proximo_bissexto(ano)    

def test():

assert eh_bissexto(0)
assert eh_bissexto(2020)
assert eh_bissexto(2024)

assert not eh_bissexto(1)
assert not eh_bissexto(2022)
assert not eh_bissexto(2023)

assert proximo_bissexto(2024) == 2024
assert proximo_bissexto(2025) == 2028
assert proximo_bissexto(2029) == 2032
assert proximo_bissexto(2020) == 2020


print(eh_bissexto)
print(proximo_bissexto)