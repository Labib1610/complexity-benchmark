import sys
from collections import deque
import itertools

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    if n > M * T:
        print("NO")
        return
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree_orig = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree_orig[v] += 1
        
    # Check for cycles and compute topological levels / longest paths to sink
    # Longest path from u to any sink
    out_deg = [len(adj[i]) for i in range(n + 1)]
    q = deque()
    dist_to_sink = [1] * (n + 1)
    
    for i in range(1, n + 1):
        if out_deg[i] == 0:
            q.append(i)
            
    visited_count = 0
    while q:
        u = q.popleft()
        visited_count += 1
        for p in rev_adj[u]:
            if dist_to_sink[u] + 1 > dist_to_sink[p]:
                dist_to_sink[p] = dist_to_sink[u] + 1
            out_deg[p] -= 1
            if out_deg[p] == 0:
                q.append(p)
                
    if visited_count < n:
        print("NO")
        return

    # Base latest time slot for each task
    L = [0] * (n + 1)
    for i in range(1, n + 1):
        L[i] = T - dist_to_sink[i] + 1
        if L[i] < 1:
            print("NO")
            return

    # Count of descendants for tie-breaking
    desc_count = [0] * (n + 1)
    for i in range(1, n + 1):
        # BFS/DFS to count all reachable nodes
        visited = [False] * (n + 1)
        dq = deque([i])
        visited[i] = True
        cnt = 0
        while dq:
            curr = dq.popleft()
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    dq.append(nxt)
        desc_count[i] = cnt

    in_degree = list(in_degree_orig)
    assigned_slot = [0] * (n + 1)
    
    # Ready tasks initially
    ready = [i for i in range(1, n + 1) if in_degree[i] == 0]
    
    # Priority key for sorting tasks: smaller L first, then larger dist_to_sink, then more descendants
    def task_key(u):
        return (L[u], -dist_to_sink[u], -desc_count[u])
    
    # Backtracking search
    def search(slot, ready_list, remaining_count):
        if remaining_count == 0:
            return True
        if slot > T:
            return False
        
        # Pruning checks
        # 1. Any ready or unready task with L[u] < slot is impossible
        # 2. Capacity check for each deadline k from slot to T
        # Let's count unassigned tasks with L[u] <= k
        # To make it fast, do simple checks:
        for u in ready_list:
            if L[u] < slot:
                return False
                
        # Separate mandatory tasks (L[u] == slot)
        mandatory = []
        optional = []
        for u in ready_list:
            if L[u] == slot:
                mandatory.append(u)
            else:
                optional.append(u)
                
        if len(mandatory) > M:
            return False
            
        needed = M - len(mandatory)
        
        if len(ready_list) <= M:
            # We must schedule all ready tasks
            chosen_batches = [ready_list]
        else:
            optional.sort(key=task_key)
            if needed >= len(optional):
                chosen_batches = [mandatory + optional]
            else:
                # Generate combinations of optional tasks
                # Limit search width if optional is large to prevent explosion
                candidates = optional[:min(len(optional), needed + 8)]
                chosen_batches = [mandatory + list(comb) for comb in itertools.combinations(candidates, needed)]
        
        for batch in chosen_batches:
            batch_set = set(batch)
            new_ready = [u for u in ready_list if u not in batch_set]
            
            for u in batch:
                assigned_slot[u] = slot
                for nxt in adj[u]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        new_ready.append(nxt)
            
            if search(slot + 1, new_ready, remaining_count - len(batch)):
                return True
                
            for u in batch:
                assigned_slot[u] = 0
                for nxt in adj[u]:
                    in_degree[nxt] += 1
                    
        return False

    if search(1, ready, n):
        print("YES")
        print(*(assigned_slot[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()