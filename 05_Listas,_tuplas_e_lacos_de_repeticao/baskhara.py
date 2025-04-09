a = int(input("Digite A"))
b = int(input("Digite B"))
c = int(input("Digite C"))

def test():
    delta = a ** 2 - 4 * a * c
if delta < 0:
    print("A equação não tem raizes verdadeiras")
else:
    x1 = (-b + delta ** 0.5) /  (2* a)
    x2 = (-b - delta ** 0.5) /  (2* a)
    print(f"As raizes são {x1} e {x2}")


