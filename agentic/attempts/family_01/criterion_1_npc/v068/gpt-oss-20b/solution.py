import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0]*n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        if u==v: continue
        adj[u] |= 1<<v
        adj[v] |= 1<<u
        neighbors[u].append(v)
        neighbors[v].append(u)

    # Quick check for clique of size 4
    def has_clique4():
        for i in range(n):
            ai = adj[i]
            for j in range(i+1, n):
                if not (ai >> j) & 1:
                    continue
                common_ij = ai & adj[j]
                # mask bits > j
                mask_k = common_ij & (~((1<<(j+1))-1))
                while mask_k:
                    k = (mask_k & -mask_k).bit_length()-1
                    mask_k -= (1<<k)
                    common_ijk = common_ij & adj[k]
                    mask_l = common_ijk & (~((1<<(k+1))-1))
                    if mask_l:
                        return True
        return False

    if has_clique4():
        print("NO")
        return

    color = [0]*n
    allowed = [0b111]*n
    result = [0]*n
    found = False

    def dfs(pos):
        nonlocal found
        if pos == n:
            for i in range(n):
                result[i] = color[i]
            found = True
            return True
        if allowed[pos] == 0:
            return False
        for c in range(1,4):
            bit = 1<<(c-1)
            if not (allowed[pos] & bit):
                continue
            color[pos] = c
            changed = []
            ok = True
            for u in neighbors[pos]:
                if color[u]==0 and (allowed[u] & bit):
                    allowed[u] ^= bit
                    changed.append(u)
                    if allowed[u]==0:
                        ok = False
                        break
            if ok and dfs(pos+1):
                return True
            # backtrack
            for u in changed:
                allowed[u] |= bit
            color[pos] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()