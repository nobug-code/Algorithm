def solution(s, cipher):

    answer = True
    dic = {}

    if(len(s) != len(cipher)):
        return False

    for i in range(len(s)):
        key = s[i]
        value = cipher[i]
        if(key in dic.keys()):
            if(dic[key] != value):
                return False

        else:#자료가 없으면 데이터를 넣어 준다.
            dic[key] = value

    return answer

print(solution("world", "abcde"))