def get_all_divisors_brute(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0 and i > 1:
            yield i
    yield n


for x in get_all_divisors_brute(61):
    print(x)