def valor_pgto(valor, forma_pgto):
    
    valor_produto = float(input("Digite o valor do produto: R$ "))
    forma_pagamento = int(input("Escolha a forma de pagamento (1: Pix, 2: À Vista no cartão, 3: Parcelado em 2x, 4: Parcelado em 3x ): "))

if forma_pagamento == 1:
    total = valor_produto * 0.85  
elif forma_pagamento == 2:
    total = valor_produto * 0.90 
elif forma_pagamento == 3:
    total = valor_produto  
elif forma_pagamento == 4:
    total = valor_produto * 1.10  
else:
    total = None
print("Valor a ser pago: R$", total )

assert valor_pgto(100, 1) == 85
assert valor_pgto(100, 2) == 90
assert valor_pgto(100, 3) == 100
assert valor_pgto(100, 4) == 110
