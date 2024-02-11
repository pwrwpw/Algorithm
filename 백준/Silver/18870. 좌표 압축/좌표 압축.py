n = int(input())
answer = list(map(int, input().split()))

sorted_answer = sorted(set(answer))
index_dict = {value: index for index, value in enumerate(sorted_answer)}

for i in answer:
    print(index_dict[i], end=' ')
