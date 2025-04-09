A = int(input("Digite A"))
B = int(input("Digite B"))
C = int(input("Digite C"))

def test():
    delta = B**2 - 4*A*C
if delta <0:
    print("A equação não tem raizes verdadeiras")
else:
    x1 = (-B + (delta ** 0.5)) /  (2* A)
    x2 = (-B - (delta ** 0.5)) /  (2* A)
print("As raizes são" x1 "e" x2)


