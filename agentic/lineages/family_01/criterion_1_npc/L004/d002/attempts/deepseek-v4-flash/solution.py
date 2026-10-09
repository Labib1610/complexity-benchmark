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

    # Try all 6 permutations of colors
    import itertools
    for perm in itertools.permutations([1, 2, 3]):
        color = [0] * n
        possible = True
        for start in range(n):
            if color[start] == 0:
                color[start] = perm[0]
                q = deque([start])
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if color[v] == 0:
                            # assign a color different from color[u]
                            for c in perm:
                                if c != color[u]:
                                    color[v] = c
                                    break
                            q.append(v)
                        elif color[v] == color[u]:
                            possible = False
                            break
                    if not possible:
                        break
            if not possible:
                break
        if possible:
            print("YES")
            print(' '.join(map(str, color)))
            return

    print("NO")

if __name__ == "__main__":
    solve()