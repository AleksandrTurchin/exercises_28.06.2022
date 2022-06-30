string = input('Введите строку: ').lower()  # use lower() - convert to lowercase
symbol = input('Введите символ: ').lower()

counter = 0

for i, x in enumerate(string[::-1]):
    if x == symbol:
        counter = 1
        break
if counter == 1:
    print(f'Индекс последнего вхождения символа: {len(string)-i}')
