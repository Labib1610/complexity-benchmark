from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    n, M, T, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        indeg[b] += 1

    # Kahn's algorithm with cycle-by-cycle processing
    indeg0 = [i for i in range(n) if indeg[i] == 0]
    # Use a min-heap? Not needed, any order works.
    # We'll use a list as a queue.
    q = deque(indeg0)
    assign = [0] * n
    cycle = 1
    processed = 0

    while q:
        if cycle > T:
            print("NO")
            return
        # Take up to M nodes for this cycle
        count = min(M, len(q))
        for _ in range(count):
            u = q.popleft()
            assign[u] = cycle
            processed += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        cycle += 1

    if processed != n:
        print("NO")
        return

    # Check if any assigned cycle > T
    if max(assign) > T:
        print("NO")
        return

    print("YES")
    print(" ".join(str(x) for x in assign))

if __name__ == "__main__":
    solve()