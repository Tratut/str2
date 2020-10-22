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
    if s1 == '':
        return False
    elif s2 == '':
        return s1
    else:
        return s1, s2
