def solution(nums):
    answer = 0
    
    nums_len = len(set(nums))
    result = int(len(nums)/2)
    
    if result < nums_len :
        answer = result
    else :
        answer = nums_len
    
    return answer