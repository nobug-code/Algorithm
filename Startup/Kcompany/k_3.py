def solution(k, room_number):
    num = len(room_number)
    answer = [0 for _ in range(num)]
    left = []
    total_room = [0 for _ in range(k+1)]
    for i in range(num):
        number = room_number[i]
        if total_room[number] == 0:
            total_room[number] = 1
            answer[i] = number
        else:
            left.append(i)

    temp = []

    for i in range(1, len(total_room)):
        if total_room[i] == 0:
            temp.append(i)
    for number, i in enumerate(left):
        for j in temp:
            if i < j:
                print(i)
                total_room[i] = 1
                answer[i] = j
                del total_room[i]
                break
    return answer

#

print(solution(10, [1,3,4,1,3,1]))

