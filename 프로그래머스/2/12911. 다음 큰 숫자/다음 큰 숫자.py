def solution(n):
    answer = 0
    count = bin(n).count("1")
    for i in range(n+1,1000001):
        i_count = bin(i).count("1")
        
        if count == i_count:
            answer = i
            break
    return answer