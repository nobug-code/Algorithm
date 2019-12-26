def solution(log_data):
    time_list = []
    start_time_list = []
    end_time_list = []

    for log in log_data:
        time = log.split(',')[1].split(" ")[1].split("ms")[0]
        start = log.split(',')[0].split(":")
        temp = start[2].split('.')
        start[2] = ''.join(temp)
        total_time = ''.join(start)
        k = 1

        temp_list = [x for x in total_time]

        for i in range(len(time) - 1, -1, -1):
            value = int(len(total_time)) - k
            num = int(time[i])
            num_2 = int(total_time[value])
            num_3 = str(num + num_2)

            temp_list[value] = num_3
            k = k + 1

        time_list.append(time)
        start_time_list.append("".join(total_time))
        end_time_list.append("".join(temp_list))

    space = [1 for i in range(len(end_time_list))]
    space_time = [0 for i in range(len(end_time_list))]

    for i in range(len(start_time_list)):
        for j in range(len(start_time_list)):
            if i == j:
                continue

            if start_time_list[i] <= start_time_list[j] <= end_time_list[i]:
                space[i] += 1
                space_time[i] = start_time_list[j]

    temp = 0
    for i in range(len(space)):
        if space[i] > space[temp]:
            temp = i

    temp_time = []
    for i in range(len(space_time[temp])):

        if i == 2 or i == 4:
            temp_time.append(":")
        elif i == 6:
            temp_time.append(".")
        temp_time.append(space_time[temp][i])
    temp_time = ''.join(temp_time)
    value = str(space[temp])

    output = str(value + ", " + temp_time)

    return output


print(solution(["00:00:00.000, 2500ms", "00:00:01.000, 1500ms", "00:00:02.000, 1000ms"]))
