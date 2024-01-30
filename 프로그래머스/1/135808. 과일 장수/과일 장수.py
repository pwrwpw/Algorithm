def solution(k, m, score):
    answer = 0
    cnt = 0
    score.sort(reverse=True)
    for sco in score:
        cnt += 1
        if cnt == m:
            cnt = 0
            answer += sco * m
            
    return answer