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
    
    # Kahn's algorithm with day assignment
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    day = [0] * n
    current_day = 1
    count_today = 0
    
    processed = 0
    while q:
        # Process all nodes that can be scheduled today
        next_q = deque()
        while q and count_today < M:
            u = q.popleft()
            day[u] = current_day
            processed += 1
            count_today += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    next_q.append(v)
        
        if count_today == M or not q:
            # Move to next day
            current_day += 1
            count_today = 0
            q = next_q
        else:
            q = next_q
        
        if current_day > T:
            print("NO")
            return
    
    if processed != n:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(day[i]) for i in range(n)))

if __name__ == "__main__":
    solve()