def solution(s, skip, index):
    answer = ''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for sk in skip:
        if sk in alpha:
            alpha = alpha.replace(sk, "")
        
    for ss in s:
        if ss in alpha:
            answer += alpha[(alpha.index(ss) + index) % len(alpha)]
        else:
            answer += ss
    
    return answer
