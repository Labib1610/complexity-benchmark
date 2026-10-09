import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    mandated = set(map(int, input().split()))
    
    g = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to prune non-mandated leaves
    parent = [0] * (R + 1)
    parent_w = [0] * (R + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in g[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    needed = [False] * (R + 1)
    for p in mandated:
        needed[p] = True
    
    # Process in reverse order to prune
    for u in reversed(order):
        if not needed[u] and u != 1:
            # check if any child needed
            has_needed_child = False
            for v, _ in g[u]:
                if v != parent[u] and needed[v]:
                    has_needed_child = True
                    break
            if not has_needed_child:
                # prune this node
                needed[u] = False
            else:
                needed[u] = True
        elif u == 1:
            # root: keep if any needed child
            has_needed_child = False
            for v, _ in g[u]:
                if needed[v]:
                    has_needed_child = True
                    break
            needed[u] = has_needed_child
    
    # Sum weights of edges where both endpoints are needed
    total = 0
    for u, v, w in edges:
        if needed[u] and needed[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()