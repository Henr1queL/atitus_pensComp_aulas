a = int(input("Digite A"))
b = int(input("Digite B"))
c = int(input("Digite C"))


    delta = a ** 2 - 4 * a * c
    if delta < 0:
        print("A equação não tem raizes verdadeiras")
    else:
        x1 = (-b + delta ** 0.5) /  (2* a)
        x2 = (-b - delta ** 0.5) /  (2* a)
        print(f"As raizes são {x1} e {x2}")


def test():
    assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]

    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0