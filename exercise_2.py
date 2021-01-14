sec_user = int(input('Введите время в секундах: '))

min_user = sec_user // 60
sec = sec_user % 60
hour = min_user // 60
min = min_user % 60

print('%02d:%02d:%02d' % (hour, min, sec))

