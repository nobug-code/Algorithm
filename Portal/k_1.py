
def solution(s):
    answer = len(s)
    for i in range(1, int(len(s)/2)+1):
        temp = 1
        first = [s[k] for k in range(i)]
        first = ''.join(first)
        print(first)
        for j in range(i, len(s), i):
            if(j + i > len(s)):
                second = [s[k] for k in range(j, len(s))]
            else:
                second = [s[k] for k in range(j, j+i)]
                if(first == second):
                    temp += 1
                    temp += len(first)
                else:
                    temp += len(first)
                    temp += len(second)

            second = ''.join(second)
            print(i, second)

            if(first == second):
                temp += 1
            else:
                temp += 1
                temp += len(first)

            first = second

        if(temp < answer):
            answer = temp
            point = i
            print("here", i, answer, second)

    return answer


def test():
    temp ="ababcdcdababcdcd"
    print(solution(temp))

test()

