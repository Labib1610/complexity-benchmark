import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    # Kahn's algorithm for topological sorting
    q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Minimum stage index for each dish based on DAG
    stage = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            stage[v] = max(stage[v], stage[u] + 1)

    # If any required stage > T, impossible
    if max(stage[1:]) > T:
        print("NO")
        return

    # Count how many dishes per minimal stage
    count = [0] * (T + 1)
    for i in range(1, n + 1):
        count[stage[i]] += 1

    # Now push stages forward to satisfy capacity
    # We'll assign as early as possible while balancing capacity
    result = [0] * (n + 1)
    queue_by_stage = [[] for _ in range(T + 1)]
    for i in range(1, n + 1):
        queue_by_stage[stage[i]].append(i)

    for s in range(1, T + 1):
        # While this stage has more than M dishes, delay some to later stages
        # We'll just keep delaying until last possible stage
        idx = 0
        while len(queue_by_stage[s]) > M:
            extra_dish = queue_by_stage[s].pop()
            if s == T:
                print("NO")
                return
            queue_by_stage[s + 1].append(extra_dish)

    # Assign final stage numbers
    for s in range(1, T + 1):
        for dish in queue_by_stage[s]:
            result[dish] = s

    print("YES")
    print(" ".join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()