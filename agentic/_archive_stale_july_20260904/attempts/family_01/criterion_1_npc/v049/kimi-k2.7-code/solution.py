import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n
    avail = [7] * n
    stack = []
    sys.setrecursionlimit(10000)

    def assign(v, c):
        q = [(v, c)]
        while q:
            v, c = q.pop()
            if colors[v] != 0:
                if colors[v] != c:
                    return False
                continue
            bit = 1 << (c - 1)
            if not (avail[v] & bit):
                return False
            stack.append((v, avail[v]))
            colors[v] = c
            avail[v] = 0
            for u in adj[v]:
                if colors[u] == 0:
                    if avail[u] & bit:
                        stack.append((u, avail[u]))
                        avail[u] &= ~bit
                        if avail[u] == 0:
                            return False
                        if avail[u] & (avail[u] - 1) == 0:
                            q.append((u, avail[u].bit_length()))
        return True

    def dfs():
        v = -1
        for i in range(n):
            if colors[i] == 0:
                v = i
                break
        if v == -1:
            return True
        mask = avail[v]
        for c in (1, 2, 3):
            if mask & (1 << (c - 1)):
                snapshot = len(stack)
                if assign(v, c) and dfs():
                    return True
                while len(stack) > snapshot:
                    u, prev = stack.pop()
                    colors[u] = 0
                    avail[u] = prev
        return False

    if dfs():
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()