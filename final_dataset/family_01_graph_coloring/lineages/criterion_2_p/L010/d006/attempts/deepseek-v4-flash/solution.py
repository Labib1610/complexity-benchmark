import sys
from collections import deque

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
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return

    # Lexicographically smallest: color 0 -> mode 1, color 1 -> mode 2
    # But we can also swap colors per component if it makes sequence smaller.
    # Since we start each component with 0, we might get a non-minimal lexicographic.
    # We can check if flipping a component gives smaller lexicographic order.
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            comp = []
            q = deque([i])
            visited[i] = True
            comp.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        comp.append(v)
                        q.append(v)
            # Check if flipping this component makes lexicographically smaller
            flip = False
            for node in comp:
                if color[node] == 1:
                    # If first differing node is 1, flipping makes it 0 -> smaller
                    flip = True
                    break
                elif color[node] == 0:
                    # If first is 0, flipping makes it 1 -> bigger, so don't flip
                    break
            if flip:
                for node in comp:
                    color[node] = 1 - color[node]

    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()