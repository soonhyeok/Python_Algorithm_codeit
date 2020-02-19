# 범위 내 요소의 개수를 카운트하는 함수
def counter_element(some_list, start, end):
    count = 0
    for element in some_list:
        if start <= element <= end:
            count += 1
    return count


def find_same_number(some_list, start=1, end=None):
    if end == None:
        end = len(some_list) - 1

    # Base Case
    # 수의 범위가 한 개이고 카운팅 수가 2개 이상이면 중복.
    if start == end:
        return start

    mid = (start + end) // 2

    # 임시 카운팅 확인용
    temp_mid = counter_element(some_list, start, mid)

    if temp_mid > mid - start + 1:
        return find_same_number(some_list, start, mid)
    else:
        return find_same_number(some_list, mid + 1, end)



# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))