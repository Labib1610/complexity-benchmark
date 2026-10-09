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
    
    # earliest start times
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            earliest[v] = max(earliest[v], earliest[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Check if any earliest exceeds T
    if max(earliest) > T:
        print("NO")
        return
    
    # Now assign slots greedily: sort tasks by earliest, place them in earliest possible slot with capacity
    tasks = list(range(n))
    tasks.sort(key=lambda x: earliest[x])
    
    slot_count = [0] * (T + 1)
    slot = [0] * n
    
    for u in tasks:
        s = earliest[u]
        while s <= T and slot_count[s] >= M:
            s += 1
        if s > T:
            print("NO")
            return
        slot[u] = s
        slot_count[s] += 1
    
    print("YES")
    print(" ".join(str(slot[i]) for i in range(n)))

if __name__ == "__main__":
    solve()