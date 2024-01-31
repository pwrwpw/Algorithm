from itertools import combinations

def is_prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    num_list = list(combinations(nums, 3))

    for num in num_list:
        
        if is_prime(sum(num)):
            answer += 1
    return answer
