def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_find_char(char, x):
    s1 = ''
    s2 = ''
    for i in range(ft_len(x)):
        if s1 == '' and x[i] == char:
            s1 = i
        if s1 != '' and i != s1 and x[i] == char:
            s2 = i
    if s1 == '':
        return -2
    elif s2 == '':
        return -1
    else:
        return s1, s2


def ft_reverse_str(x):
    res = ''
    for i in range(ft_len(x)):
        res += x[(i + 1) * -1]
    return res


def ft_reverse_between_char(char, x):
    k = ft_find_char(char, x)
    if k == -1 or k == -2:
        return k
    else:
        k1 = k[0]
        k2 = k[1]
    first = ''
    second = ''
    rev = ''

    for i in range(0, k1):
        first += x[i]
    for i in range(k2 + 1, ft_len(x)):
        second += x[i]
    for i in range(k1, k2 + 1):
        rev += x[i]
    rev = ft_reverse_str(rev)
    return first + rev + second

# print(ft_reverse_between_char("a", "12a345a67a89"))
# out 12a76a543a89
