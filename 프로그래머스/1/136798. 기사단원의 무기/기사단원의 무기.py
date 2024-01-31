def solution(number, limit, power):
    answer = 0
    num_list = []
    
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**(1/2)+1)):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt+=1
        num_list.append(cnt)
    for num in num_list:
        if num > limit:
            num = power
        answer += num

    return answer
