def solution(n, lost, reserve):
    answer = n

    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for student in lost_set:
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            answer -= 1

    return answer
