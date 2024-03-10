def reverse_words(sentence):
    parts = sentence.split('<')  # '<'을 기준으로 문자열을 분리합니다.
    result = ''
    for part in parts:
        if '>' in part:
            # 태그 내부의 단어는 그대로 두고, 태그는 그대로 추가합니다.
            tag, word = part.split('>', 1)
            result += '<' + tag + '>'
            words = word.split()
            for i in range(len(words)):
                result += words[i][::-1]  # 단어를 뒤집습니다.
                if i < len(words) - 1:
                    result += ' '  # 단어 사이에 공백을 추가합니다.
        else:
            # 태그 외부의 단어는 뒤집습니다.
            words = part.split()
            for i in range(len(words)):
                result += words[i][::-1]  # 단어를 뒤집습니다.
                if i < len(words) - 1:
                    result += ' '  # 단어 사이에 공백을 추가합니다.
    return result

s = input()

print(reverse_words(s))
