import sys
sys.setrecursionlimit(1_000_000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0 uncolored, 1 or 2
    possible = True
    
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color the component
            color[start] = 1
            stack = [start]
            while stack:
                u = stack.pop()
                cu = color[u]
                nv = 2 if cu == 1 else 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = nv
                        stack.append(v)
                    elif color[v] != nv:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # For each connected component, we can flip all colors (1<->2) independently.
    # To get lexicographically smallest overall, process components in order of their smallest vertex.
    # For each component, decide whether to flip based on the color of its smallest vertex.
    
    comp_id = [0] * (n + 1)
    comps = []
    comp_min = []
    cid = 0
    for i in range(1, n + 1):
        if comp_id[i] == 0:
            cid += 1
            comp_id[i] = cid
            stack = [i]
            nodes = []
            mn = i
            while stack:
                u = stack.pop()
                nodes.append(u)
                if u < mn:
                    mn = u
                for v in adj[u]:
                    if comp_id[v] == 0:
                        comp_id[v] = cid
                        stack.append(v)
            comps.append(nodes)
            comp_min.append(mn)
    
    # For each component, if the smallest vertex has color 2, flip the component.

    for nodes in comps:
        mn = min(nodes)
        if color[mn] == 2:
            for u in nodes:
                color[u] = 3 - color[u]  # flip 1<->2
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1))) + "\n")

if __name__ == "__main__":
    solve()