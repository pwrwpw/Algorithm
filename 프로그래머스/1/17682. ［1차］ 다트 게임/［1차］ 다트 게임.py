def solution(dartResult):
    scores = []
    current_score = 0

    for char in dartResult:
        if char.isdigit():
            current_score = current_score * 10 + int(char)
        elif char == 'S':
            scores.append(current_score)
            current_score = 0
        elif char == 'D':
            scores.append(current_score ** 2)
            current_score = 0
        elif char == 'T':
            scores.append(current_score ** 3)
            current_score = 0
        elif char == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif char == '#':
            scores[-1] *= -1

    return sum(scores)