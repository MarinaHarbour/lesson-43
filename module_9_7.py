def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res > 1:
            for i in range(2, res):
                if (res % i) == 0:
                    print(f"Составное число {res}")
                    break
            else:
                print(f"Простое число {res}")
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result_2 = sum_three(3, 6, 1)
print(result_2)
