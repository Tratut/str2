from ft_len import ft_len


def ft_find_char(chrr, x):
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
