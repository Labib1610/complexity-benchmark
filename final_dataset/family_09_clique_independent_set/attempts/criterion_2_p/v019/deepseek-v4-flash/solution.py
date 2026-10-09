import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    part0 = []
    part1 = []

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            part0.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            part0.append(v)
                        else:
                            part1.append(v)
                        q.append(v)

    size0 = len(part0)
    size1 = len(part1)

    # We need to pick k vertices from the two independent sets.
    # We can take x from part0 and k-x from part1, with 0 <= x <= size0, 0 <= k-x <= size1
    # Since both parts are independent sets, any such combination is valid.
    if k > size0 + size1:
        print("NO")
        return

    # Try to take as many as possible from part0 first
    take0 = min(size0, k)
    take1 = k - take0
    if take1 > size1:
        # Not possible with this split, try another
        take1 = min(size1, k)
        take0 = k - take1
        if take0 > size0:
            print("NO")
            return

    res = part0[:take0] + part1[:take1]
    print("YES")
    print(" ".join(str(x + 1) for x in res))

if __name__ == "__main__":
    solve()