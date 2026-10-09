for a in range(n):
    for b in range(a+1, n):
        cab = common[a][b]
        if cab > 3:
            continue
        for c in range(b+1, n):
            if cab + common[b][c] + common[a][c] == 3:
                print(a+1, b+1, c+1)
                return