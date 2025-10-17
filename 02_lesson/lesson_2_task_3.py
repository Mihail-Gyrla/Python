import math


def square(side):
    return math.ceil(side * side)


side = float(input("Введите сторону квадрата: "))
print(f"Площать двадрата со стороной {side} равна {square(side)}")


