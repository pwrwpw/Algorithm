def solution(k, tangerine):
    answer = 0
    
    arr = [0] * (max(tangerine) + 1)
    for i in tangerine:
        arr[i] += 1

    arr.sort(reverse=True)
    for i in range(0, len(arr)):
        if arr[i] > 0:
            k -= min(arr[i], k)
            answer += 1
        if k == 0:
            break
    
    return answer