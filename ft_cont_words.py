def ft_cont_words(x):
    kol = 0
    for i in x:
        if i == ' ':
            kol += 1
    if x != '':
        return kol + 1
    else:
        return 0
