def braces(values):

    open_list = ['(', '{', '[']
    total_result = []


    for value in values:
        stack_list = []

        for temp in value:
            flag = 0
            for i in open_list:
                if temp == i:
                    flag = 1
                    break

            if flag == 1:
                stack_list.append(temp)

            else:
                if temp == ")":
                    pair = "("
                elif temp == "]":
                    pair = "["
                elif temp == "}":
                    pair = "{"

                if len(stack_list) == 0:
                    stack_list.append(temp)
                    break
                if stack_list[len(stack_list) -1] == pair:
                    del stack_list[len(stack_list) -1]
                else:
                    stack_list.append(temp)

        if len(stack_list) == 0:
            total_result.append("YES")
        else:
            total_result.append("NO")

    return total_result

values = ['[{()()}({[]})]({}[({})])((((((()[])){}))[]{{{({({({{{{{{}}}}}})})})}}}))[][][]]']
print(braces(values))