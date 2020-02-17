def sublist_max(profits):
    total_list = []

    for i in range(len(profits)):
        total = 0
        for j in range(i, len(profits)):
            total += profits[j]
            total_list.append(total)

    return max(total_list)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))