def print_factor(x):
    for i in range(2, x):
        if x % i == 0:
            print(i)

print_factor(52633)
