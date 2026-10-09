import sys
from sys import setrecursionlimit

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m
    
    # Build adjacency list among edges (two edges are adjacent if they share a vertex)
    eadj = [[] for _ in range(m)]
    for u in range(1, n + 1):
        lst = adj[u]
        for i in range(3):
            ei = lst[i][1]
            for j in range(i + 1, 3):
                ej = lst[j][1]
                eadj[ei].append(ej)
                eadj[ej].append(ei)
    
    setrecursionlimit(3000000)
    
    def dfs(e, c):
        color[e] = c
        for f in eadj[e]:
            if color[f] == 0:
                if not dfs(f, 3 - c):
                    return False
            elif color[f] == c:
                return False
        return True
    
    for e in range(m):
        if color[e] == 0:
            if not dfs(e, 1):
                print("NO")
                return
    
    print("YES")
    print(' '.join(str(x) for x in color))

if __name__ == "__main__":
    main()