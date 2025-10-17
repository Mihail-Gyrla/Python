god = int(input("Введите год: "))


def is_year_leap(god):
    return True if god % 4 == 0 else False


print(f"Год {god}: {is_year_leap(god)}")
