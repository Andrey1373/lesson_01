user_number = None
while True:
    user_number = int(input('Введите целое положительное число: '))
    if user_number <= 9:
        print('Число должно быть больше 9!')
    elif user_number >= 100:
        print('Число должно быть меньше 100!')
    else:
        break

left_operand = user_number // 10
right_operand = user_number % 10

if left_operand == right_operand:
    print(f'В числе {user_number}, операнды равны')
elif left_operand >= right_operand:
    print(f'В числе {user_number}, наибольший операнд {left_operand}')
else:
    print(f'В числе {user_number}, наибольший операнд {right_operand}')