def programmerStrings(s):
    # Write your code here
    label = 'p r o g r a m m e r'.split()
    i = 0
    count = 0

    p = label.count('p')
    r = label.count('r')
    o = label.count('o')
    g = label.count('g')
    a = label.count('a')
    m = label.count('m')
    e = label.count('e')
    total = 0

    while i < (len(s) - len(label) - 1):

        temp_list = label
        temp = s[i:len(label) + count]
        print(temp)

        temp_p = temp.count('p')
        temp_r = temp.count('r')
        temp_o = temp.count('o')
        temp_g = temp.count('g')
        temp_a = temp.count('a')
        temp_m = temp.count('m')
        temp_e = temp.count('e')

        if p <= temp_p and r <= temp_r and o <= temp_o and \
                g <= temp_g and a <= temp_a and m <= temp_m and e <= temp_e:

            total += len(temp)
            i = i + len(label)
            count = i
            print("kkk", total)
        else:
            count += 1

    print(total)

# 문제 설명

programmerStrings("progxrammerrxproxgrammer")
