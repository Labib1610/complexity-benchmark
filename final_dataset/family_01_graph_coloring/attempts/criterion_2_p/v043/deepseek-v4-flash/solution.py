import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        print("NO")
        return
    
    # Now we have a bipartite graph, color 0 -> mode 1, color 1 -> mode 2
    # But we need lexicographically smallest assignment.
    # We can try to flip components if it makes earlier nodes smaller.
    comp_id = [-1] * n
    comps = []
    comp_count = 0
    for i in range(n):
        if comp_id[i] == -1:
            stack = [i]
            comp_id[i] = comp_count
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in g[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = comp_count
                        stack.append(v)
            comps.append(nodes)
            comp_count += 1
    
    # For each component, decide orientation
    assign = [0] * n
    for nodes in comps:
        # nodes sorted by index
        nodes.sort()
        # Try orientation where first node is 1
        # If first node color is 0 -> mode 1, if color 1 -> mode 2
        # We can flip if needed
        first = nodes[0]
        if color[first] == 1:
            # flip this component
            for u in nodes:
                color[u] = 1 - color[u]
        for u in nodes:
            assign[u] = 1 if color[u] == 0 else 2
    
    print("YES")
    print(" ".join(map(str, assign)))

if __name__ == "__main__":
    solve()