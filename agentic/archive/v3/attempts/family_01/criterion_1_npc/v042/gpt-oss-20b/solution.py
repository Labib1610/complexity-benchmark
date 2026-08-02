import sys
sys.setrecursionlimit(10000)

def solve():
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
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    allowed = [0b111] * n  # bits 0..2 for colors 1..3
    colored = [0] * n
    stack = []  # store (vertex, previous_allowed)
    found = False

    def dfs(idx):
        nonlocal found
        if idx == n:
            found = True
            return True
        # try colors 1..3
        for col in range(1, 4):
            bit = 1 << (col - 1)
            if not (allowed[idx] & bit):
                continue
            # assign
            colored[idx] = col
            # record changes
            changes = []
            conflict = False
            for nb in adj[idx]:
                if colored[nb] == 0:
                    old = allowed[nb]
                    new = old & ~bit
                    if old != new:
                        changes.append((nb, old))
                        allowed[nb] = new
                        if new == 0:
                            conflict = True
                            break
            if not conflict:
                if dfs(idx + 1):
                    return True
            # rollback
            for v, old in reversed(changes):
                allowed[v] = old
            colored[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colored[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()