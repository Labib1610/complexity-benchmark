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
    
    stage = [0] * n
    current_stage = 1
    count_in_stage = 0
    processed = 0
    
    while q:
        # If current stage is full, move to next
        if count_in_stage == M:
            current_stage += 1
            count_in_stage = 0
            if current_stage > T:
                print("NO")
                return
        
        u = q.popleft()
        stage[u] = current_stage
        count_in_stage += 1
        processed += 1
        
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Check if any stage exceeds T
    if max(stage) > T:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x) for x in stage))

if __name__ == "__main__":
    solve()