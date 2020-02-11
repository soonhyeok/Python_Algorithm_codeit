def fib_tab(n):
    fib_table = [0, 1, 1]

    if n < 3:
        return 1

    for i in range(3, n + 1):
        fib_index = fib_table[i - 1] + fib_table[i - 2]
        fib_table.append(fib_index)

    return fib_table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))