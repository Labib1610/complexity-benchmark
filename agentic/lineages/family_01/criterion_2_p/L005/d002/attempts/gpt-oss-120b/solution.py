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

    color = [ -1 ] * (n + 1)          # 0 or 1 for bipartition
    answer = [0] * (n + 1)            # final tier (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
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
        # decide which side gets tier 1
        # find smallest index in component
        min_node = min(comp_nodes)
        # if min_node is in color 0, give color0 -> 1, else color1 -> 1
        give_one = color[min_node]          # the color that will be tier 1
        for v in comp_nodes:
            answer[v] = 1 if color[v] == give_one else 2

    # output
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()