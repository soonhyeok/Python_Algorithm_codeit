def trapping_rain(buildings):
    # 변수 : 총 갇히는 비의 양
    total_rain = 0

    # 변수 : 처음부터 올라가는 인덱스
    # 변수 : 마지막부터 내려오는 인덱스
    low = 0
    high = len(buildings) - 1

    # low 부터 왼쪽으로 가장 높은 건물 높이
    left_max = 0

    # high 부터 오른쪽으로 가장 높은 건물 높이
    right_max = 0

    while low <= high:
        if buildings[low] < buildings[high]:
            if buildings[low] >= left_max:
                # 해당 인덱스에 빗물 담지 않고, low부터 왼쪽으로 가장 높은 건물 업데이트.
                left_max = buildings[low]

            else:
                total_rain += left_max - buildings[low]
            low += 1

        else:
            if buildings[high] >= right_max:
                # 해당 인덱스에 빗물 담지 않고, high부터 왼쪽으로 가장 높은 건물 업데이트.
                right_max = buildings[high]

            else:
                total_rain += right_max - buildings[high]
            high -= 1

    return total_rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))