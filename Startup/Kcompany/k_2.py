from itertools import product

def solution(user_id, banned_id):

    answer = 1

    temp_list_len = [[] for i in range(len(banned_id))]

    # 각 각 해당 하는 아이디의 수를 구하고
    # 각 리스트의 숫자를 곱해 주면 된다.
    num = 0
    for b_id in banned_id:
        for i in  range(len(user_id)):
            u_id = user_id[i]
            flag = 0
            if(len(b_id) != len(u_id)):
                continue
            for k in range(len(b_id)):
                if(b_id[k] == "*"):
                    continue
                else:
                    if(b_id[k] != u_id[k]):
                        flag = 1
                        break
            if(flag == 0):
                temp_list_len[num].append(u_id)

        num += 1

    num = 1

    for i in range(len(temp_list_len)):
        num *= len(temp_list_len[i])


    total = [[] for i in range(num)]

    temp = []
    total_list = list(product(*temp_list_len))
    answer = len(total_list)

    for i in total_list:

        temp.append(sorted(list(i)))

    kkk = [list(item) for item in set(tuple(row) for row in temp)]
    answer = len(kkk)
    for i in kkk:
        temp = set(i)
        if(len(temp) != len(i)):
            answer -= 1



    return answer


print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))