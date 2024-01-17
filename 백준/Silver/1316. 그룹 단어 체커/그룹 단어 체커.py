import sys

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    word_list = []
    word = sys.stdin.readline().strip()
    for j in range(len(word)):
        if j > 0:
            if (word[j] in word_list) and (word[j] != word[j-1]):
                count -= 1
                break
        word_list.append(word[j])
    count += 1

print(count)