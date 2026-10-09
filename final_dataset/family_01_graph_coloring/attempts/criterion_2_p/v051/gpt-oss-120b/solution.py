import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n + 1)          # 0/1 temporary colors
    ans = [0] * (n + 1)               # final frequencies 1/2
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # decide orientation: give frequency 1 to the side containing the smallest index node
        # start is the smallest index in this component because we iterate in order
        side_one = color[start]          # this side will become frequency 1
        for node in comp_nodes:
            ans[node] = 1 if color[node] == side_one else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()