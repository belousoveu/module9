class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.__pointer = start

    def __iter__(self):
        self.__pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.__pointer > self.stop:
                raise StopIteration
        else:
            if self.__pointer < self.stop:
                raise StopIteration
        result = self.__pointer
        self.__pointer += self.step
        return result


if __name__ == "__main__":
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)
    iter6 = Iterator(10, 20, -1)  # не будет проходить итерация
    iter7 = Iterator(20, 10)  # не будет проходить итерация
    iter8 = Iterator(ord('a'), ord('z'), 1)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
    for i in iter6:
        print(i, end=' ')
    print()
    for i in iter7:
        print(i, end=' ')
    print()
    for i in iter8:
        print(chr(i), end=' ')
    print()
