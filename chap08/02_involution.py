def power(x, y):
    # Base Case
    if y == 0:
        return 1

    elif y == 1:
        return x

    if y % 2 == 0:
        return power(x * x, y / 2)

    else:
        return x * power(x * x, (y - 1) // 2)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))