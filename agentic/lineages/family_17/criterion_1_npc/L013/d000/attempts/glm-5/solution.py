def cover(c):
    # unlink column header from header list
    L[R[c]] = L[c]; R[L[c]] = R[c]
    i = D[c]
    while i != c:
        j = R[i]
        while j != i:
            U[D[j]] = U[j]; D[U[j]] = D[j]
            # decrement size of column C[j]
            S[C[j]] -= 1
            j = R[j]
        i = D[i]