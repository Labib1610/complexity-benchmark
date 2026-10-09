import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
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
    
    # Topological sort with earliest possible slot
    slot = [1] * n
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if slot[v] < slot[u] + 1:
                slot[v] = slot[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Check if any task exceeds deadline
    for i in range(n):
        if slot[i] > T:
            print("NO")
            return
    
    # Count tasks per slot
    cnt = [0] * (T + 2)
    for i in range(n):
        cnt[slot[i]] += 1
    
    # Check capacity constraints
    for t in range(1, T + 1):
        if cnt[t] > M:
            print("NO")
            return
    
    # Greedy balancing: push tasks forward to fill capacity
    for t in range(1, T):
        if cnt[t] < M:
            can_add = M - cnt[t]
            # Pull from future slots
            for future in range(t + 1, T + 1):
                if can_add == 0:
                    break
                if cnt[future] > 0:
                    move = min(can_add, cnt[future])
                    cnt[t] += move
                    cnt[future] -= move
                    can_add -= move
    
    # Reconstruct slot assignments
    # Group tasks by their original slot
    tasks_by_slot = [[] for _ in range(T + 1)]
    for i in range(n):
        tasks_by_slot[slot[i]].append(i)
    
    # Distribute tasks according to new counts
    new_slot = [0] * n
    for t in range(1, T + 1):
        need = cnt[t]
        # Take 'need' tasks from earliest available slots >= t
        for s in range(t, T + 1):
            if need == 0:
                break
            while tasks_by_slot[s] and need > 0:
                task = tasks_by_slot[s].pop()
                new_slot[task] = t
                need -= 1
    
    # Verify the solution
    # Check precedence
    for u in range(n):
        for v in adj[u]:
            if new_slot[v] <= new_slot[u]:
                print("NO")
                return
    
    # Check capacity
    cap_cnt = [0] * (T + 1)
    for i in range(n):
        cap_cnt[new_slot[i]] += 1
    for t in range(1, T + 1):
        if cap_cnt[t] > M:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(new_slot[i]) for i in range(n)))

solve()