# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    string_number = str(n)
    if int(n) < 10:
        return int(n)
    else:
        return int(sum_digits(string_number[1:])) + int(string_number[0])


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))