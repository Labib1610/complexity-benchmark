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
    
    # Now we have a valid bipartition, but we need lexicographically smallest.
    # We can try to flip components if it makes earlier vertices 1.
    # Since color[0] is 0 initially, we can try to flip components to get smaller lexicographic order.
    # We'll do BFS/DFS and for each component, decide orientation.
    
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
            # Determine if flipping this component (swap 0<->1) gives lexicographically smaller
            # We compare current assignment vs flipped assignment for this component
            # Current: color[u] as is
            # Flipped: 1 - color[u]
            flip = False
            for u in sorted(comp):
                if (1 - color[u]) < color[u]:
                    flip = True
                    break
                elif (1 - color[u]) > color[u]:
                    break
            if flip:
                for u in comp:
                    color[u] = 1 - color[u]
    
    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()