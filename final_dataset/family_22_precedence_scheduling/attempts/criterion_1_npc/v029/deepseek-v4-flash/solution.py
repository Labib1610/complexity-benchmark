from collections import deque, defaultdict
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
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
    
    # Kahn's algorithm to get topological order and assign earliest possible step
    q = deque()
    step = [0] * (n + 1)
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
            step[i] = 1
    
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                step[v] = step[u] + 1
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Check if any step exceeds T
    if max(step[1:]) > T:
        print("NO")
        return
    
    # Check capacity per step
    count = [0] * (T + 1)
    for i in range(1, n + 1):
        count[step[i]] += 1
        if count[step[i]] > M:
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(step[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()