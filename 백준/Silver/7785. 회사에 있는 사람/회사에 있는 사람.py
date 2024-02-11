import sys

n = int(sys.stdin.readline())

answer = set()

for _ in range(n):
    name, state = map(str, sys.stdin.readline().split())
    if state == 'enter':
        answer.add(name)
    elif state == 'leave' and name in answer:
        answer.remove(name)

# Sort and print the names in reverse order
for i in sorted(answer, reverse=True):
    print(i)
