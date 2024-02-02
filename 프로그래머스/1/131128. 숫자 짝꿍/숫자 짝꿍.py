def solution(X, Y):
    answer = []
    seen = set()
    for i in range(9,-1,-1):
        answer += str(i) * min(X.count(str(i)),Y.count(str(i)))
        
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return "".join(answer)