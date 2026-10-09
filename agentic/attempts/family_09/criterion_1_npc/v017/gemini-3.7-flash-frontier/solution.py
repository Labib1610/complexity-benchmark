import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_mask = (1 << n) - 1
    comp = [0] * n
    for i in range(n):
        comp[i] = (all_mask ^ adj[i]) ^ (1 << i)

    def bron_kerbosch(R, P, X):
        if len(R) == k:
            return R
        if len(R) + P.bit_count() < k:
            return None

        # Choose pivot u from P | X maximizing |P & comp[u]|
        u_cand = P | X
        best_u = -1
        max_inter = -1

        temp = u_cand
        while temp:
            v = (temp & -temp).bit_length() - 1
            cnt = (P & comp[v]).bit_count()
            if cnt > max_inter:
                max_inter = cnt
                best_u = v
            temp &= temp - 1

        branch_cand = P & (~comp[best_u])
        while branch_cand:
            v = (branch_cand & -branch_cand).bit_length() - 1
            R.append(v)
            res = bron_kerbosch(R, P & comp[v], X & comp[v])
            if res is not None:
                return res
            R.pop()
            P ^= 1 << v
            X |= 1 << v
            branch_cand &= branch_cand - 1
            if len(R) + P.bit_count() < k:
                break
        return None

    ans = bron_kerbosch([], (1 << n) - 1, 0)

    if ans is not None:
        print("YES")
        print(*(x + 1 for x in ans))
    else:
        print("NO")

if __name__ == '__main__':
    main()