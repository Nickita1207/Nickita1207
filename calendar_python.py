def sum(a, b):
    return a + b

print('  -Сложение чисел-')
print()
num_1 = input('Введите первое число\n')
print()
num_2 = input('Введите второе число\n')
print()
answer = sum(int(num_1), int(num_2))
print('_____________________')
print('Ответ: ' + num_1 + '+' + num_2 + '=' + str(answer))
print()
input('Нажмите Enter для выхода\n')
