def soluntion(record):

    answer = []# answer 영구 보관함
    temp_list = [] # 임시 보관함
    #중복은 마지막에 set으로 해서 하면 돤다 .

    for email in record :
        temp = email.split(' ')[0]
        #print(temp)
        if(temp == "RECEIVE"):
            temp_email = email.split(' ')[1]
            temp_list.append(temp_email)

        elif(temp == "DELETE"):
            if(len(temp_list) == 0):
                continue
            del temp_list[len(temp_list) - 1] #가장 최근에 들어 간거 삭제

        elif(temp == "SAVE"):

            for item in temp_list:
                answer.append(item)
            temp_list = [] #임시 보관함 비우기

        #print("answer is", answer)
        #print("temp_list is", temp_list)

    answer = list(set(answer))
    return answer


#temp = ["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "RECEIVE QwerTY@naver.com"]
#temp_2 =["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "SAVE", "DELETE",  "RECEIVE QwerTY@naver.com", "SAVE"]
#temp_3 = ["RECEIVE abcd@naver.com"]

