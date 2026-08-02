import sys
sys.setrecursionlimit(1000000)

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

    allowed = [7] * n          # bits 0,1,2 for colors 1,2,3
    color = [0] * n            # 0 means unassigned

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        u = idx
        mask = allowed[u]
        # try colors in order 1,2,3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if mask & bit:
                color[u] = c
                changes = []
                conflict = False
                for v in adj[u]:
                    if color[v] == 0:
                        if allowed[v] & bit:
                            prev = allowed[v]
                            allowed[v] ^= bit
                            changes.append((v, prev))
                            if allowed[v] == 0:
                                conflict = True
                                break
                if not conflict:
                    if dfs(idx + 1):
                        return True
                # revert changes
                for v, prev in changes:
                    allowed[v] = prev
                color[u] = 0
        return False

    if dfs(0):
        out_lines = ["YES", " ".join(str(c) for c in color)]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()