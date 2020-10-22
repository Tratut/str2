def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_change_str(str1, str2, str3):
    word_ln = ft_len(str1)
    if str1 not in str3:
        return False
    else:
        while str1 in str3:
            ind = str3.index(str1)
            first = ''
            sec = ''
            for i in range(0, ind):
                first += str3[i]
            for i in range(ind + word_ln, ft_len(str3)):
                sec += str3[i]
            str3 = first + str2 + sec
    return str3

# print(ft_change_str("1", "2", "21212121212121212"))
