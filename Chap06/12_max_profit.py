def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    if count in cache:
        return cache[count]
    else:
        if count < len(price_list):
            max_value = price_list[count - 1]
        else:
            max_value = 0

        for i in range(1, (count // 2) + 1):
            max_value = max(max_value, max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache))

        cache[count] = max_value

        return max_value



def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


def sublist_max(profits):

    max_value = 0
    temp_value = 0

    for i in profits:
        temp_value += i
        if max_value < temp_value:
            max_value = temp_value

    return max_value


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
