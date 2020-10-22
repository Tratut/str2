def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_count_words(st):
    count = 0
    while st[0] == " ":
        cop = ''
        for i in range(1, ft_len(st)):
            cop += st[i]
        st = cop
    while " " in st:
        ind = st.index(" ")
        copp = ''
        for g in range(ind + 1, ft_len(st)):
            copp += st[g]
        st = copp
        if ft_len(st) > 0:
            while st[0] == " ":
                cop = ''
                for i in range(1, ft_len(st)):
                    cop += st[i]
                st = cop
            count += 1
    return count + 1

# print(ft_count_words("   f  adsd dfhsdg dsgdsfg    ewgfsgfafedga"))
