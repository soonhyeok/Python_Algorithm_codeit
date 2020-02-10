def consecutive_sum(start, end):
    # Base Case
    if start == end:
        return start

    mid_num = (start + end) // 2

    return consecutive_sum(start, mid_num) + consecutive_sum(mid_num + 1, end)


# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))