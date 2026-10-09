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
        color[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return

    # Now we have a valid bipartition.
    # To get lexicographically smallest, we try to flip colors if possible
    # without breaking bipartiteness.
    # We can do a BFS/DFS and try to assign 1 to smallest indices.
    # Since bipartite coloring is unique per component up to swapping,
    # we can choose the orientation that gives smaller lexicographic order.

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
            # Try both colorings for this component
            # color1: keep current color
            # color2: flip
            # choose lexicographically smaller
            # We'll compare by building assignment arrays
            assign1 = [0] * n
            assign2 = [0] * n
            for u in comp:
                assign1[u] = color[u] + 1
                assign2[u] = 2 - color[u]  # flip: 1->2, 2->1
            # Compare lexicographically
            # We only need to compare within this component
            # Find first index where they differ
            comp_sorted = sorted(comp)
            flip = False
            for u in comp_sorted:
                if assign1[u] != assign2[u]:
                    flip = assign2[u] < assign1[u]
                    break
            if flip:
                for u in comp:
                    color[u] ^= 1

    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()