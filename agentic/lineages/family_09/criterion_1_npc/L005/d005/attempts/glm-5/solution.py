for T in range(1, 1 << n2):
    v = (T & -T).bit_length() - 1
    f[T] = max(f[T ^ (1 << v)], f[T & ~nbr[v]] + 1)