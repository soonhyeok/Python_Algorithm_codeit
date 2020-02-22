def sum_in_list(search_sum, sorted_list):
    left_index = 0
    right_index = len(sorted_list) - 1

    while left_index <= right_index:
        sum = sorted_list[left_index] + sorted_list[right_index]

        if sum < search_sum:
            left_index += 1

        elif sum > search_sum:
            right_index -= 1

        elif sum == search_sum:
            return True

        if left_index == right_index:
            return False





print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))