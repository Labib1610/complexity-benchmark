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
    
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    shift_assignment = [0] * n
    current_shift = 1
    processed = 0
    
    while q:
        if current_shift > T:
            break
        batch = []
        for _ in range(min(M, len(q))):
            node = q.popleft()
            batch.append(node)
            shift_assignment[node] = current_shift
            processed += 1
        
        for node in batch:
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        current_shift += 1
    
    if processed == n and max(shift_assignment) <= T:
        print("YES")
        print(" ".join(str(shift_assignment[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()