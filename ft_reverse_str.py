from ft_len import ft_len


def ft_reverse_str(x):
    res = ''
    for i in range(ft_len(x)):
        res += x[(i + 1) * -1]
    return res
