import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color each component bipartite graph
    color = [-1] * n
    visited = [False] * n
    
    def dfs(node, c):
        color[node] = c
        for nei in adj[node]:
            if color[nei] == -1:
                if not dfs(nei, 1 - c):
                    return False
            elif color[nei] == c:
                return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                print("NO")
                return
    
    # Construct the lexicographically smallest solution
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()