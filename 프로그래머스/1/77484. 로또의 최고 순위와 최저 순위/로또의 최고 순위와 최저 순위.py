def solution(lottos, win_nums):
    answer = 0
    rank = [6,6,5,4,3,2,1]
    
    cnt_zero = lottos.count(0)
    
    for num in win_nums:
        if num in lottos:
            answer += 1
    return rank[answer+cnt_zero],rank[answer]