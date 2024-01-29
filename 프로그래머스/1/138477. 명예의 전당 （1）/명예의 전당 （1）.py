def solution(k, score):
    answer = []
    list = []
    for i in range(len(score)):
        if i < k:
            list.append(score[i])
        else:
            if min(list) < score[i]:
                list.remove(min(list))
                list.append(score[i])
        answer.append(min(list))         
    return answer