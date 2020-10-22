def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_remove_str(str1, str2):
    if str1 not in str2:
        return False
    else:
        word_ln = ft_len(str1)
        while str1 in str2:
            ind = str2.index(str1)
            first = ''
            sec = ''
            for i in range(0, ind):
                first += str2[i]
            for i in range(ind + word_ln, ft_len(str2)):
                sec += str2[i]
            str2 = first + sec
    return str2

# print(ft_remove_str("aa", "qaweraaadfaagaaa"))
