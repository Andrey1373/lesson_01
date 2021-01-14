proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))

if proceeds > costs:
    profit = proceeds - costs
    print(f'Ваша прибыль составила {profit} руб.')
    effection = int((profit / proceeds) * 100)
    print(f'Рентабельность выручки составила {effection}%')
    people = int(input('Введите количество сотрудников компании: '))
    people_profit = round(profit / people, 2)
    print(f'Прибыль компании в рассчете на одного сотрудника составила {people_profit} руб./чел.')
elif proceeds < costs:
    print('У вас нет прибыли, вы работаете в убыток!')
else:
    print('У вас нет прибыли, но вы не в минусе, вы вышли в ноль!')



