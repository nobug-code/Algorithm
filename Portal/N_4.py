'''

단계
1. 솔입을 세척 , 5분, 없음
2. 반죽을 준비 , 30분 , 없음
3. 콩과꺠를 준비 , 15분, 없음
4. 반죽에 콩을 재움, 30분, 2, 3
5. 반죽에 꺠를 체움 , 35분, 2,3
6. 솔에 솔잎을 깔고 송편을, 20, 1,4,5
7. ~~~, 4분 6번

1,2,3 단계는 동시에 진행이 가능
2,3, 단계를 수행하 다음에는 4,5를 동시에 진행 가능


결과값은 k가 매개변수로 주어진다. k 단계를 수행하기 위해 반드시 먼저 완료 해야 하는 단계 개수와 k 단계를 완료 하는데 최소 몇 분이 걸리는지

'''

temp_cook = [5, 30, 15, 30, 35, 20, 4]
order = [[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7]]
k = 6

temp_cook2 = [5,3,2]
order_2 = [[1,2,], [2,3], [1,3]]
k_2 = 3

temp_cook3 = [5,30,15,30,35,20,4,50,40]
order_3 = [[2,4],[2,5],[3,4],[3,5],[1,6],[4,6],[5,6],[6,7],[8,9]]
k_3 = 9


def solution(cook_times, order, k):

    answer = []
    max_num_list = cook_times

    temp_list = [[0]* k for i in range(len(cook_times))]
    count_list = [[0] * k for i in range(len(cook_times))]

    #mark
    for i in range(len(order)):
        first = order[i][0]-1
        second = order[i][1]-1


        temp_list[second][first] = 1
        count_list[second][first] = 1

    #print(max_num_list)
    for i in range(len(temp_list)):

        for j in range(len(temp_list[i])):
            if(temp_list[i][j] == 1):
                temp_list[i][j] = cook_times[i] + max_num_list[j]

        #print(temp_list)
        if(max_num_list[i] < max(temp_list[i])):
            max_num_list[i] = max(temp_list[i])
        #print(max_num_list)

    #print(max_num_list)
    max_num_list = max_num_list[:k]
    #print(max_num_list)
    time = max(max_num_list)
    #print(time)

    for i in range(len(count_list[6])):
        if (count_list[6][i] == 1):
            for j in range(len(count_list[i])):
                if (count_list[i][j] == 1):
                    count_list[6][j] = 1
    print(count_list)

    count = count_list[k-1].count(1)
    answer.append(count)
    answer.append(time)

    return answer

print(solution(temp_cook, order, k))