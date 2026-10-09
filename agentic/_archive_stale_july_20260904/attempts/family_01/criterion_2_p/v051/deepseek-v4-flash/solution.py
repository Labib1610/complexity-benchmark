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
    
    def bfs(start):
        from collections import deque
        q = deque([start])
        color[start] = 1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # We can try to flip colors in each connected component if it makes sequence smaller.
    visited = [False] * n
    
    def flip_component(start):
        stack = [start]
        visited[start] = True
        comp = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    comp.append(v)
        # Try flipping
        flip = False
        for u in comp:
            if color[u] == 2 and (color[u] - 1) < color[u]:
                # Actually we compare sequences: flipping means 1->2, 2->1
                # We check if flipping makes lexicographically smaller
                pass
        # Simpler: for each component, if flipping makes first differing position smaller, flip.
        # Compare current vs flipped
        cur = [color[u] for u in comp]
        flipped = [3 - c for c in cur]
        # We need to compare in original index order
        comp_sorted = sorted(comp)
        cur_seq = [color[u] for u in comp_sorted]
        flip_seq = [3 - color[u] for u in comp_sorted]
        if flip_seq < cur_seq:
            for u in comp:
                color[u] = 3 - color[u]
    
    for i in range(n):
        if not visited[i]:
            flip_component(i)
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()