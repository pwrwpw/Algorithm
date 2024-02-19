from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        start = people.pop()
        if len(people) > 0 and start + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer