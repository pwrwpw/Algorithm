def solution(N, stages):
    answer = [0] * (N + 1)

    for i in stages:
        if i <= N:
            answer[i] += 1

    total_players = len(stages)
    failure_rate = []
    for i in range(1, N + 1):
        if total_players == 0:
            failure_rate.append((0, i))
        else:
            failure_rate.append((answer[i] / total_players, i))
            total_players -= answer[i]

    failure_rate.sort(key=lambda x: x[0], reverse=True)

    return [stage for rate, stage in failure_rate]
