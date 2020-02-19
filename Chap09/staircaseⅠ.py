fib_cache = {}

def staircase(n):
    if n < 2:
        return 1

    if n in fib_cache:
        return fib_cache[n]

    else:
        temp = staircase(n - 1) + staircase(n - 2)
        fib_cache[n] = temp
        return temp

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
