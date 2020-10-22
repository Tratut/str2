def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_change_place_word(x):
    k1 = ''
    k2 = ''
    i = 0
    let = x[i]
    while let != ' ':
        k1 += let
        i += 1
        let = x[i]
    for i in range(ft_len(k1) + 1, ft_len(x)):
        k2 += x[i]
    return k2 + ' ' + k1
