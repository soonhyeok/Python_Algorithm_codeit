def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged_list.append(list2[j])
            j += 1

        else:
            merged_list.append(list1[i])
            i += 1

    if j == len(list2):
        merged_list += list1[i:]
        i = len(list1)

    elif i == len(list1):
        merged_list += list2[j:]
        j = len(list2)

    return merged_list


# 합병 정렬
def merge_sort(my_list):
    # Base Case
    # 리스트 : 2개 이하인 경우
    if len(my_list) < 2:
        return my_list

    # 리스트 길이 아주 작게 분할
    # 정렬된 두 리스트를 새로 정렬한 값 리턴
    return merge(merge_sort(my_list[:len(my_list) // 2]), merge_sort(my_list[len(my_list) // 2:]))


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))