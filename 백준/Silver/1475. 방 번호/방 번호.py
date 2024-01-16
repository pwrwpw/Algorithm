import sys

N = sys.stdin.readline().strip()

num_set = [0] * 10

for i in N:
    num = int(i)
    if num == 6 or num == 9:
        if num_set[6] == num_set[9]:
            num_set[6] += 1
        else:
            num_set[9] += 1
    else:
        num_set[num] += 1

print(max(num_set))
