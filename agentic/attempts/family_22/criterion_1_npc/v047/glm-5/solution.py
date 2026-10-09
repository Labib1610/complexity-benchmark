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
    in_degree = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        in_degree[v] += 1
    
    # Topological sort to get earliest days
    earliest = [1] * n
    q = deque()
    r_in_degree = list(in_degree)
    for i in range(n):
        if r_in_degree[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            r_in_degree[v] -= 1
            if r_in_degree[v] == 0:
                q.append(v)
    
    if len(topo_order) != n:
        print("NO")
        return
    
    # Check if earliest days are feasible
    earliest_count = [0] * (T + 2)
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
        earliest_count[earliest[i]] += 1
    
    # Check capacity constraints for earliest days
    for d in range(1, T + 1):
        if earliest_count[d] > M:
            print("NO")
            return
    
    # Calculate latest days
    latest = [T] * n
    for u in reversed(topo_order):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    for i in range(n):
        if latest[i] < 1:
            print("NO")
            return
    
    # Greedy assignment: assign each container to its latest possible day
    # Process in order of latest days (ascending)
    containers_by_latest = [[] for _ in range(T + 1)]
    for i in range(n):
        containers_by_latest[latest[i]].append(i)
    
    day_count = [0] * (T + 2)
    assignment = [0] * n
    
    for d in range(1, T + 1):
        # First, assign containers whose latest day is d
        for u in containers_by_latest[d]:
            # Find the latest day <= d that is >= earliest[u] and has capacity
            day_assigned = -1
            for cand in range(d, earliest[u] - 1, -1):
                if day_count[cand] < M:
                    day_assigned = cand
                    break
            if day_assigned == -1:
                print("NO")
                return
            assignment[u] = day_assigned
            day_count[day_assigned] += 1
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()