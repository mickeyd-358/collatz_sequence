starting_number = int(input("Enter number: "))
n = starting_number

while n != 1:
    print(n)
    if n % 2 == 0:  # n is even
        n = n // 2
    else:  # n is odd
        n = 3 * n + 1

print(n)

print("bad luck")
