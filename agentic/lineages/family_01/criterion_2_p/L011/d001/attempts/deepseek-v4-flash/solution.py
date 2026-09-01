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
    
    color = [-1] * n  # -1 uncolored, 0 -> value 1, 1 -> value 2
    
    def bfs(start):
        from collections import deque
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # Now we have a valid coloring, but we need lexicographically smallest.
    # We can try flipping each component if it makes the smallest index in that component 1.
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
            # Check if flipping would make lexicographically smaller
            # If the smallest index in comp currently has color 1 (value 2), flip
            min_node = min(comp)
            if color[min_node] == 1:
                for u in comp:
                    color[u] = 1 - color[u]
    
    result = [1 if color[i] == 0 else 2 for i in range(n)]
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()