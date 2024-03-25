n = int(input())

if n % 3 == 0:
    num_3 = n // 3
    num_5, remainder = divmod(num_3, 5)
    print(num_5 * 3 + remainder)
elif (n - 5) >= 0 and (n - 5) % 3 == 0:
    num_3 = (n - 5) // 3
    num_5, remainder = divmod(num_3, 5)
    print(num_5 * 3 + remainder + 1)
elif (n - 10) >= 0 and (n - 10) % 3 == 0:
    num_3 = (n - 10) // 3
    num_5, remainder = divmod(num_3, 5)
    print(num_5 * 3 + remainder + 2)
else:
    print(-1)