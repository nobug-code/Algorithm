def solution(arr):

    #1일 경우에만 더해 주면 된다.
    answer = 1
    temp = []
    i = 0
    while(True):

        if(i >= len(arr)):
            break

        if(arr[i] == 1):
            # 좌 우 더 해 준거에서 큰 거를 남긴다.
            if(i == 0):
                temp.append(arr[0] + arr[1])
                i += 2
            elif(i == len(arr) - 1):
                temp[len(temp) - 1] = temp[len(temp) - 1] + arr[i]
                i += 1

            else:
                #좌 일때
                if(temp[len(temp) - 1] < arr[i+1]):
                    temp[len(temp)-1] = temp[len(temp) - 1] + arr[i]
                    i += 1
                else:
                    temp.append(arr[i] + arr[i+1])
                    i += 2
                #우 일때
        else:
            temp.append(arr[i])
            i += 1
    print(temp)
    for num in temp:
        answer *= num

    return answer

print(solution([1,1,1,5]))










































