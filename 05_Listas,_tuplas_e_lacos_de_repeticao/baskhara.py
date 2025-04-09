import math

a = int(input("Digite A:"))
b = int(input("Digite B:"))
c = int(input("Digite C:"))

def test():
    delta = a ** 2 - 4 * a * c
if delta < 0:
    print("A equação não tem raizes verdadeiras")
else:
   x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [x1, x2]
     print("As raizes são", x1, "e", x2)


