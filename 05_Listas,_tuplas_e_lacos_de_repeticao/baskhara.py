import math

def baskhara(a, b, c):
     delta = a ** 2 - 4 * a * c
     if delta < 0:
        print("A equação não tem raizes verdadeiras")
        return None
     else:
        x1 = (-b + math.sqrt(delta)) /  (2 * a)
        x2 = (-b - math.sqrt(delta)) /  (2 * a)

     if x1 < x2:
        return [x1, x2]
     else:
        return [x2, x1]

  
def test():

    assert baskhara(1, -3, 2) == [1.0, 2.0]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]
    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == [0.0, 0.0]