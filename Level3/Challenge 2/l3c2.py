def l3c2(l):
    div = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                div[i] += 1
                count = div[j]
    return count
