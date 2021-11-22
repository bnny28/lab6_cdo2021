def div(x, y):
    if y == 0:
        return None
    else:
        return x / y


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        print('На 0 делить нельзя!')
    else:
        print(f'Результат деления: {div(a, b)}')
except Exception:
    print('Ошибка! Ожидалось число!')
