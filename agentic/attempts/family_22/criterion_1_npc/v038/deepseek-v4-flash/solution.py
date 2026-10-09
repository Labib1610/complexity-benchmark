from collections import deque, defaultdict
import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Kahn's algorithm to get topological order and earliest phase
    q = deque()
    phase = [0] * n
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
            phase[i] = 1
    
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                phase[v] = phase[u] + 1
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Check if any phase exceeds T
    if max(phase) > T:
        print("NO")
        return
    
    # Now we need to assign phases respecting capacity M
    # We can push some tasks to later phases if needed
    # Greedy: assign each task to the earliest possible phase >= its earliest phase
    # but not exceeding T, and respecting capacity.
    
    # Build list of tasks sorted by earliest phase
    tasks = list(range(n))
    tasks.sort(key=lambda x: phase[x])
    
    # capacity per phase
    cap = [M] * (T + 1)
    assigned = [0] * n
    
    for u in tasks:
        # find earliest phase >= phase[u] with capacity
        p = phase[u]
        while p <= T and cap[p] == 0:
            p += 1
        if p > T:
            print("NO")
            return
        assigned[u] = p
        cap[p] -= 1
    
    print("YES")
    print(" ".join(str(assigned[i]) for i in range(n)))

if __name__ == "__main__":
    solve()