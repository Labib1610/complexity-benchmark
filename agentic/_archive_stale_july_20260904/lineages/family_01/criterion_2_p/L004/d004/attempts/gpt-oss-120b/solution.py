import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * n          # 0 or 1 for bipartition, -1 = unvisited
    ans = [0] * n              # final colors 1 or 2

    for start in range(n):
        if parity[start] != -1:
            continue
        stack = [start]
        parity[start] = 0
        comp = [start]
        min_idx = start
        while stack:
            v = stack.pop()
            if v < min_idx:
                min_idx = v
            pv = parity[v]
            for nb in adj[v]:
                if parity[nb] == -1:
                    parity[nb] = pv ^ 1
                    stack.append(nb)
                    comp.append(nb)
                elif parity[nb] == pv:
                    sys.stdout.write("NO")
                    return
        # decide which parity gets color 1 to make lexicographically smallest
        if parity[min_idx] == 0:
            col0, col1 = 1, 2
        else:
            col0, col1 = 2, 1
        for v in comp:
            ans[v] = col0 if parity[v] == 0 else col1

    out_lines = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()