def solution(n, m, section):
    answer = 0
    temp = 0
    for sect in section:
        if sect >= temp:
            temp = sect + m
            answer += 1
    return answer