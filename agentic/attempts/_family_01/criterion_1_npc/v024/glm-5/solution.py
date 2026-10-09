import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Find all maximal independent sets using Bron-Kerbosch with pivoting
    mis_list = []
    def bron_kerbosch(R, P, X):
        if P == 0 and X == 0:
            mis_list.append(R)
            return
        # Choose pivot u from P | X that maximizes |P & adj[u]|
        pivot = -1
        best = -1
        candidates = P | X
        temp = candidates
        while temp:
            u_bit = temp & -temp
            u = u_bit.bit_length() - 1
            count = bin(P & adj[u]).count('1')
            if count > best:
                best = count
                pivot = u
            temp ^= u_bit
        # Iterate over P \ adj[pivot]
        diff = P & ~adj[pivot]
        temp = diff
        while temp:
            v_bit = temp & -temp
            v = v_bit.bit_length() - 1
            newP = P & ~adj[v]
            newX = X & ~adj[v]
            bron_kerbosch(R | (1 << v), newP, newX)
            P ^= v_bit
            X |= v_bit
            temp ^= v_bit
    
    bron_kerbosch(0, (1 << n) - 1, 0)
    
    # Check if there are 3 disjoint maximal independent sets covering all vertices
    L = len(mis_list)
    for i in range(L):
        s1 = mis_list[i]
        rem1 = ((1 << n) - 1) ^ s1
        for j in range(i+1, L):
            s2 = mis_list[j]
            if (s1 & s2) == 0:
                rem2 = rem1 ^ s2
                for k in range(j+1, L):
                    s3 = mis_list[k]
                    if (s3 & rem2) == s3:
                        # Found valid cover
                        color = [0] * n
                        temp = s1
                        while temp:
                            b = temp & -temp
                            v = b.bit_length() - 1
                            color[v] = 1
                            temp ^= b
                        temp = s2
                        while temp:
                            b = temp & -temp
                            v = b.bit_length() - 1
                            color[v] = 2
                            temp ^= b
                        temp = s3
                        while temp:
                            b = temp & -temp
                            v = b.bit_length() - 1
                            color[v] = 3
                            temp ^= b
                        print("YES")
                        print(" ".join(map(str, color)))
                        return
    print("NO")

solve()