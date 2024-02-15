n = int(input())

values = list(map(int, input().split()))

operations = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def dfs(depth,total,plus,minus,multi,divide):
    global max_value, min_value
    if depth == n:
        max_value = max(total,max_value)
        min_value = min(total,min_value)
        return
    if plus:
        dfs(depth + 1, total + values[depth],plus-1,minus,multi,divide)
    if minus:
        dfs(depth + 1, total - values[depth],plus,minus-1,multi,divide)
    if multi:
        dfs(depth + 1, total * values[depth],plus,minus,multi-1,divide)
    if divide:
        dfs(depth + 1, int(total / values[depth]),plus,minus,multi,divide-1)

dfs(1,values[0],operations[0],operations[1],operations[2],operations[3])

print(max_value)
print(min_value)