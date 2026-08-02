import sys
sys.setrecursionlimit(1000000)

def main():
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

    allowed = [0b111 for _ in range(n)]  # bits 0,1,2 for colors 1,2,3
    color = [0] * n

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        for c in range(1, 4):
            mask = 1 << (c - 1)
            if not (allowed[v] & mask):
                continue
            old_allowed_v = allowed[v]
            old_color_v = color[v]
            allowed[v] = mask
            color[v] = c
            modified = []
            fail = False
            for u in adj[v]:
                if color[u] == c:
                    fail = True
                    break
                if allowed[u] & mask:
                    old = allowed[u]
                    allowed[u] &= ~mask
                    modified.append((u, old))
                    if allowed[u] == 0:
                        fail = True
                        break
            if not fail and dfs(idx + 1):
                return True
            # backtrack
            for u, old in modified:
                allowed[u] = old
            allowed[v] = old_allowed_v
            color[v] = old_color_v
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()