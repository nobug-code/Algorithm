def solution(str_boy):
    temp_list = ['b', 'o', 'y']
    flag = 0
    for temp_str in str_boy:
        for temp in temp_list:
            if temp_str == temp:
                flag = 1
        if flag == 1:
            return -1

    strBoy = str_boy.lower()

    total = 0
    total_b = []
    total_o = []
    total_y = []
    for i in range(len(strBoy)):
        if strBoy[i] == 'b':
            total_b.append(i)
        elif strBoy[i] == "o":
            total_o.append(i)
        else:
            total_y.append(i)

    o_back = [0 for _ in range(len(total_o))]

    for o in range(len(total_o)):
        for k in total_y:
            if total_o[o] < k:
                o_back[o] += 1

    for i in range(len(total_b)):
        for j in range(len(total_o)):
            if total_b[i] < total_o[j]:
                for k in range(j, len(o_back)):
                    total += o_back[k]
                break
    return total


solution('BOYBBOOYY')
'''
def solution(self, strBoy):
        
        # change to lower 일치 시키기 위해 (단위)
        strBoy = strBoy.lower()
        temp_list = ['b', 'o', 'y']
        
        # 올바른 값이 들어 왔나 확인용
        flag = 0
        for temp_str in strBoy:
            for temp in temp_list:
                if temp_str == temp:
                    flag = 1
            if flag == 0:
                return -1

    
        total = 0
        for i in range(len(strBoy)):
            
            # 입력의 b가 들어 올 경우 뒤의 o, y 를 구한다.
            if strBoy[i] == 'b':
                total_o = []
                total_y = []
                # b 뒤의 o, y 의 자리 위치를 저장
                for j in range(i, len(strBoy)):
                    if strBoy[j] == "o":
                        total_o.append(j)
                    elif strBoy[j] == "y":
                        total_y.append(j)
            
                o_back = [0 for _ in range(len(total_o))]
                
                # o 자리 뒤에 y가 몇개 있는지 체크
                for o in range(len(total_o)):
                    for k in total_y:
                        if total_o[o] < k:
                            o_back[o] += 1
                # o 뒤에 나올 수 있는 경우의 수를 모두 구해서 더해준다. 
                total += sum(o_back)

        return total

'''
