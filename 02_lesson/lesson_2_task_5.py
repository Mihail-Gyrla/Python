n = int(input("Введите номер месяца: "))


def month_to_season(n):
    if 1 <= n <= 2 or n == 12:
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
    else:
        return "Такого месяца нет в году!"


print(month_to_season(n))
