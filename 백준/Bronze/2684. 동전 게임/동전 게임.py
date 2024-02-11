def count_sequences(coin_tosses):
    sequences = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
    counts = [0] * 8

    for i in range(38):
        toss = coin_tosses[i:i+3]
        index = sequences.index(toss)
        counts[index] += 1

    return counts

P = int(input())  # 테스트 케이스 개수

for _ in range(P):
    coin_tosses = input().strip()  # 동전 40번 던진 결과
    result = count_sequences(coin_tosses)
    # 결과를 올바른 순서로 출력
    result = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]]
    print(" ".join(map(str, result)))