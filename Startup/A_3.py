def solution(k):

    result = ""
    temp = [0]
    i = 1
    num = 0
    position = 0

    while(i != k):

        if(temp[0] == 9):
            for j in range(len(temp)):
                temp[j] = j
            temp.append(len(temp))
            position = len(temp) - 1
        else:
            #끝에가 9에 접근했을 경우
            if(temp[position] == 9):
                if(len(temp) == 1):
                    temp[position] += 1
                else:
                    print("i is ", i)
                    temp[position-1] += (temp[position-1] + 1)
                    temp[position] = temp[position-1]
                position = len(temp)-1
            else:
                temp[position] += 1
        i += 1

    for i in range(len(temp)):
        temp[i] = str(temp[i])


    result = ''.join(temp)
    return result


print(solution(29))