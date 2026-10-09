T = M
S_A = []
while T and len(S_A) < needed:
    v = T.bit_length() - 1
    T1 = T - (1 << v)  # exclude v
    T2 = T1 & ~adjA[v]  # exclude v and neighbors
    if 1 + f[T2] == f[T]:
        S_A.append(v)
        T = T2
    else:
        T = T1