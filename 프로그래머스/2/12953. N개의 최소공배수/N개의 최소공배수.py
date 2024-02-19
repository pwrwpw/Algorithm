def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result


def solution(arr):
    answer = find_lcm_of_list(arr)
    return answer