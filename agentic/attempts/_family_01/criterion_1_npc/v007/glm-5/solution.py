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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # color: 0 = unassigned, 1/2/3 = shift
    color = [0] * n

    def dfs(i):
        if i == n:
            return True
        if color[i] != 0:
            return dfs(i + 1)
        # try colors 1,2,3
        for c in (1, 2, 3):
            ok = True
            mask = adj[i]
            while mask:
                j = (mask & -mask).bit_length() - 1
                mask &= mask - 1
                if color[j] == c:
                    ok = False
                    break
            if ok:
                color[i] = c
                if dfs(i + 1):
                    return True
                color[i] = 0
        return False

    if dfs(0):
        out = ["YES"]
        out.append(" ".join(str(x) for x in color))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()