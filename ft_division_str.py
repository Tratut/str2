from ft_len import ft_len


def ft_division_str(x):
    lenn = ft_len(x)
    if lenn % 2 == 0:
        part = lenn // 2
    else:
        part = lenn // 2 + 1
    firs = ''
    sec = ''
    for i in range(0, part):
        firs += x[i]
    for i in range(part, ft_len(x)):
        sec += x[i]
    return sec + firs
