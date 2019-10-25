'''
소수길(prime number path)은 네자리 수(0으로 시작할수는 없다, 즉 1000 이상)
 소수로 이루어진 유한한 길이의 수열이며 수열에서 인접한 수들은 최대 한 자리씩만 차이날 수 있다
(2311과 2371은 한 자리 차이이므로 인접할 수 있고, 2311과 2377은 두 자리가 다르므로 인접할 수 없다.)
두네자리소수 S와 T가 주어 졌을때 S로 시작해서 T로 끝나는 가장 짧은 소수길을 구하는 프로그램을 작성하시오
(해당하는 소수길이 존재하지 않는 경우는 입력으로 주어지지 않는다.)

입력
두네자리소수 S와 T가 띄어쓰기로 구분되어주어진다(형식은입출력예시참고.)
S로 시작해서 T로 끝나는 가장 짧은 소수길을 한 줄 에 하나씩 순서대로 출력한다
(길이가 가장 짧은 소수길이 여러가지라면 그 중 아무거나 하나만 출력해도 된다.)

입출력 방식
입력
2311 2377
출력
2311
2371
2377
'''



#두 숫자의 소수 리시트를 먼저 구한다.
first, second = map(int, input().split(' '))
first_num = first
last_num = second
prime_list = []
prime_list.append(first)


for num in range(first+1, second):
    flag = True
    for i in range(2, int(num/2)+1):
        if(num % i == 0):
            flag = False
            break
    if(flag):
        prime_list.append(num)
prime_list.append(second)



def check(first, second):

    f_4 = int(first / 1000)
    f_3 = int((first % 1000)/100)
    f_2 = int((first % 100)/10)
    f_1 = int(first % 10)

    s_4 = int(second / 1000)
    s_3 = int((second % 1000) / 100)
    s_2 = int((second % 100) / 10)
    s_1 = int(second % 10)

    count = 0
    if(f_4 == s_4):
        count += 1
    if(f_3 == s_3):
        count += 1
    if(f_2 == s_2):
        count += 1
    if(f_1 == s_1):
        count += 1

    if(count >= 3):
        return True
    else:
        return False

#bfs 로 접근 해보자
#메모리가 공유 안되는 리스트를 만들자.

import queue
q = queue.Queue()
matrix = [[first_num] for i in range(len(prime_list)+1)]
q.put((0, 0, matrix))

while(q.empty() == False):

    index_num, count, start_point = q.get()
    if(check(prime_list[index_num], last_num)):
        matrix[start_point].append(last_num)
        print(matrix[start_point])
        break

    for i in range(index_num+1, len(prime_list)):
        if(check(prime_list[index_num], prime_list[i])):
            if(index_num == 0):
                matrix[i].append(prime_list[i])
                q.put((i, count + 1, i))
            else:
                matrix[start_point].append(prime_list[i])
                q.put((i, count + 1, start_point))
