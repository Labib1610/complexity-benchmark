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
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            # BFS to color component
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
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
    
    # Now we have a valid bipartite coloring (0/1)
    # We want lexicographically smallest sequence of 1/2.
    # Since 1 < 2, we prefer 1 for earlier nodes if possible.
    # But we must keep bipartite constraints.
    # We can flip colors in each component if it makes earlier nodes 1.
    
    # We'll do a BFS/DFS to decide orientation per component.
    final = [0] * n
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
            # Determine if flipping helps lexicographically
            # Current color from earlier BFS: color[node]
            # Option A: keep as is (color 0 -> 1, color 1 -> 2)
            # Option B: flip (color 0 -> 2, color 1 -> 1)
            # Compare sequences for nodes in comp sorted by index
            comp_sorted = sorted(comp)
            keep = []
            flip = []
            for u in comp_sorted:
                keep.append(1 if color[u] == 0 else 2)
                flip.append(2 if color[u] == 0 else 1)
            if flip < keep:
                for u in comp:
                    final[u] = 2 if color[u] == 0 else 1
            else:
                for u in comp:
                    final[u] = 1 if color[u] == 0 else 2
    
    print("YES")
    print(" ".join(map(str, final)))

if __name__ == "__main__":
    solve()