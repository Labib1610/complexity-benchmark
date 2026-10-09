from collections import deque
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
    
    # earliest possible slot for each job
    earliest = [1] * n
    # capacity used per slot
    cap_used = [0] * (T + 2)
    
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    processed = 0
    slots = [0] * n
    
    while q:
        u = q.popleft()
        # find earliest slot >= earliest[u] with capacity
        s = earliest[u]
        while s <= T and cap_used[s] >= M:
            s += 1
        if s > T:
            print("NO")
            return
        slots[u] = s
        cap_used[s] += 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            earliest[v] = max(earliest[v], s + 1)
            if indeg[v] == 0:
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x) for x in slots))

if __name__ == "__main__":
    solve()