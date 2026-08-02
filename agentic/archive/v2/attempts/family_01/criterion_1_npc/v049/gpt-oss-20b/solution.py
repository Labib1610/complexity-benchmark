import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    allowed = [0b111] * n          # bits 0,1,2 correspond to colors 1,2,3
    assignment = [0] * n

    def dfs(i: int) -> bool:
        if i == n:
            return True
        # try colors 1..3
        for color in (1, 2, 3):
            mask = 1 << (color - 1)
            if not (allowed[i] & mask):
                continue
            # record changes to neighbors j > i
            changes = []
            conflict = False
            for j in adj[i]:
                if j > i:
                    if allowed[j] & mask:
                        changes.append((j, allowed[j]))
                        allowed[j] &= ~mask
                        if allowed[j] == 0:
                            conflict = True
            if not conflict:
                assignment[i] = color
                if dfs(i + 1):
                    return True
            # restore
            for j, prev in changes:
                allowed[j] = prev
            assignment[i] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(x) for x in assignment)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()