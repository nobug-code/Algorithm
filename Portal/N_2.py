#문자가 주어진다.
'''
A ~ Z 까지 주어지는데 최소한의 갯수로 제거를 해야 한다. 그래서 사전 정렬식으로 정렬이 되어야 한다.
일단 앞에께 뒤에꺼 보다 앞에 있는 숫저여야 한다.
'''

temp_list = []

def soluntions(S):

    for i in range(len(S)-1):
        if(i == len(S)-2):
            if(S[i] > S[i+1]):
                temp_list.append(S[i+1])
                continue

        if(S[i] > S[i+1]):
            temp_list.append(S[i])

    return len(temp_list)

print(soluntions("cba"))








