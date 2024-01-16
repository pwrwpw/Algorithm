def solution(numbers, target):
    answer = 0
    que = [0]
    for num in numbers:
        tmp = []
        for s in que:
            tmp.append(s-num)
            tmp.append(s+num)
        que = tmp
    for leaf in que:
        if leaf == target:
            answer += 1
    return answer