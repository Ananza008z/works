n = int(input())

is_prime = 0
for num_in in range(2, n+1):
    for checker in range(2, num_in):
        if num_in % checker == 0: break
        elif num_in % checker != 0 and checker == num_in-1:
            is_prime += 1
            break
print(is_prime+1)