def ft_reverse_str(x):
    res = ''
    for i in range(ft_len(x)):
        res += x[(i + 1) * -1]
    return res


def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_analysis(x):
    # 1
    print(x[2])
    # 2
    print(x[-2])
    # 3
    k = ''
    for i in range(5):
        k += x[i]
    print(k)
    k = ''
    # 4
    for i in range(ft_len(x) - 2):
        k += x[i]
    print(k)
    k = ''
    # 5
    for i in range(0, ft_len(x), 2):
        k += x[i]
    print(k)
    k = ''
    # 6
    for i in range(1, ft_len(x), 2):
        k += x[i]
    print(k)
    # 7
    k = ft_reverse_str(x)
    print(k)
    # 8
    nnn = ''
    for i in range(0, ft_len(x), 2):
        nnn += k[i]
    print(nnn)
    # 9
    print(ft_len(x))

