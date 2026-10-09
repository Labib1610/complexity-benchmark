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
    answer = [0] * n

    for start in range(n):
        if color[start] != -1:
            continue

        # BFS component
        q = deque([start])
        color[start] = 0  # 0 and 1 internally, we'll map to 1 and 2 later
        comp = [start]
        possible = True

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    comp.append(v)
                    q.append(v)
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break

        if not possible:
            print("NO")
            return

        # Try both colorings for this component (root 0 or root 1)
        # comp is already with root 0.
        # Flip: root 1
        comp_sorted = sorted(comp)

        # Compare two assignments lexicographically for this component
        # Assignment A: as we have (root=0)
        # Assignment B: flipped
        better = None
        for node in comp_sorted:
            ca = color[node]  # 0 or 1
            cb = 1 - color[node]  # flip
            # map 0->1, 1->2
            a_val = ca + 1
            b_val = cb + 1
            if a_val < b_val:
                better = "A"
                break
            elif b_val < a_val:
                better = "B"
                break
        if better is None:
            better = "A"  # they are all equal? Actually for a 2-coloring, flip gives opposite values, so there will be diff at first node. But safe.

        # Assign
        for node in comp:
            if better == "A":
                colors[node] = color[node] + 1
            else:
                colors[node] = (1 - color[node]) + 1

    print("YES")
    print(' '.join(map(str, colors)))

if __name__ == "__main__":
    solve()