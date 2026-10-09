from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    n, M, T, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        indeg[b] += 1
    
    # Step 1: Topological sort with earliest time assignment
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    processed = 0
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        processed += 1
        for v in graph[u]:
            earliest[v] = max(earliest[v], earliest[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Step 2: Check earliest deadline feasibility
    if max(earliest) > T:
        print("NO")
        return
    
    # Step 3: Greedy assignment inside capacity constraints
    # Sort nodes by earliest time, then assign them to the earliest possible cycle
    order = sorted(range(n), key=lambda x: earliest[x])
    assigned = [0] * n
    # slots[t] = number used so far in cycle t+1
    slots = [0] * (T + 1)
    
    for u in order:
        # Place at earliest possible slot that satisfies time and capacity
        placed = False
        for t in range(earliest[u], T + 1):
            if slots[t] < M:
                assigned[u] = t
                slots[t] += 1
                placed = True
                break
        if not placed:
            print("NO")
            return
    
    # Verify dependencies (strictly earlier)
    for u in range(n):
        for v in graph[u]:
            if assigned[u] >= assigned[v]:
                print("NO")
                return
    
    print("YES")
    print(" ".join(map(str, assigned)))

if __name__ == "__main__":
    solve()