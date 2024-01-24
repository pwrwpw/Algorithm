import sys

k, n = map(int, sys.stdin.readline().split())

lan_list = []

for _ in range(k):
    lan_list.append(int(sys.stdin.readline()))

min_value = 1
max_value = max(lan_list)

while min_value <= max_value:
    mid = (max_value + min_value) // 2
    lan = 0

    for value in lan_list:
        lan += value // mid

    if lan >= n:
        min_value = mid + 1
    else:
        max_value = mid - 1

print(max_value)
