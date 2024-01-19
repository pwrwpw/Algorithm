from collections import deque

def solution(numbers):
    answer = ''
    q = deque()
    
    nums = list(map(str, numbers))
    nums = sorted(nums,reverse=1)
    
    for num in nums:
        q.append(num*4)
        
    q = sorted(q,reverse=1)
    q_half = [num[:len(num)//4] for num in q]
    
    answer = str(int(''.join(q_half)))
    return answer