import random

# Task1
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda a, b: a == b, first, second)))


# Task2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for item in data_set:
                f.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Task3
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, *args):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

second_ball = MysticBall(1, 10, 25, 75)

for i in range(5):
    print(second_ball())