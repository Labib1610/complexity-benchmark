def cover(col):
    # remove column header
    R[L[col]] = R[col]
    L[R[col]] = L[col]
    # remove every row that has a 1 in this column
    i = D[col]
    while i != col:
        j = R[i]
        while j != i:
            U[D[j]] = U[j]
            D[U[j]] = D[j]
            S[C[j]] -= 1
            j = R[j]
        i = D[i]

def uncover(col):
    i = U[col]
    while i != col:
        j = L[i]
        while j != i:
            S[C[j]] += 1
            U[D[j]] = j
            D[U[j]] = j
            j = L[j]
        i = U[i]
    R[L[col]] = col
    L[R[col]] = col