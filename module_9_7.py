def if_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            print("Число не является ни простым, ни составным")
            return n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print("Составное число")
                return n
        print("Простое число")
        return n
    return wrapper



@if_prime
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 3, 6))
print(sum_three(2, 3, 5))
print(sum_three(000, 1, 0))
print(sum_three(-20, 3, 4))