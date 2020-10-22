def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_find_second_char(chrr, x):
    s1 = ''
    s2 = ''
    for i in range(ft_len(x)):
        if s1 == '' and x[i] == chrr:
            s1 = i
        if s1 != '' and i != s1 and x[i] == chrr:
            s2 = i
            return s2
    if s1 == '':
        return -2
    elif s2 == '':
        return -1
