def solution(s):
    answer = 0
    first_cnt = 0
    not_cnt = 0
    first = ''
    for i in s:
        if first_cnt == not_cnt:
            first_cnt += 1
            first = i
            answer += 1
        elif first == i:
            first_cnt += 1
        else:
            not_cnt += 1
    return answer