first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x[0]) - len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1]))
# Сравниваем длину элементов первого и второго списка попарно. Если списки содержат разное количество элементов,
# то проверка происходит по размеру более короткого списка
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)
                                                                if len(first) <= len(second) else len(second)))

print(len('Computers'))
print(len('Компьютер'))

print(list(first_result))
print(list(second_result))
