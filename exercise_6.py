real_result = int(input('Введите сколько км вы можете пробежать за день: '))
future_result = int(input('Введите сколько км вы хотели бы пробегать за день: '))

percent = 1 + 10 / 100
i = 1

print(f'{i}-й день: {real_result} км')

while real_result < future_result:
    real_result = round(real_result * percent, 1)
    i += 1
    print(f'{i}-й день: {real_result} км')

print(f'На {i}-й день вы достигните результата не менее {int(real_result)} км')



