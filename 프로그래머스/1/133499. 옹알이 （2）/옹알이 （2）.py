def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:
        for word in words:
            if word*2 not in bab:
                bab = bab.replace(word, ' ')
        if len(bab.strip()) == 0:
            answer += 1
    return answer
