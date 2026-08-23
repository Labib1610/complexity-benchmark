import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n  # -1 unassigned, 0 -> dosage 1, 1 -> dosage 2
    
    for i in range(n):
        if color[i] == -1:
            # try to assign 1 (color 0) to this node
            color[i] = 0
            stack = [i]
            ok = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                print("NO")
                return
    
    # If we reach here, graph is bipartite
    # But we need lexicographically smallest: we may flip colors in components
    # where starting with 1 gives smaller lexicographic order.
    # We already started with 1 for each component, but we need to check if flipping
    # a component yields smaller lexicographic order.
    
    # To handle lexicographically smallest, we can do BFS/DFS and for each component,
    # compare the two possible colorings and pick the lexicographically smaller.
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # collect component
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # Now we have component nodes. We have two possible colorings:
            # coloring A: color[i] as is (starting with 0)
            # coloring B: flip all colors in this component
            # We need to pick lexicographically smaller.
            # Since we already assigned colors, we can compare.
            # But we must ensure consistency: color array already has values for this comp.
            # We'll build two candidate arrays for this comp.
            comp.sort()
            # candidate A
            candA = [color[u] for u in comp]
            # candidate B
            candB = [1 - color[u] for u in comp]
            # compare lexicographically
            if candB < candA:
                for u in comp:
                    color[u] = 1 - color[u]
    
    # Output
    print("YES")
    res = [1 if c == 0 else 2 for c in color]
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()