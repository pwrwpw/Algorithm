import sys

n = int(sys.stdin.readline())
n_arr = sorted(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in range(m):
    if binary_search(n_arr, m_arr[i], 0, n - 1):
        print("1", end=" ")
    else:
        print("0", end=" ")