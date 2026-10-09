import sys
from collections import deque
import random
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    M = int(next(iterator))
    T = int(next(iterator))
    m = int(next(iterator))
    
    if n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        radj[v].append(u)
        in_degree[v] += 1
        out_degree[u] += 1
        
    # Topological sort & cycle check
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    
    # Compute Earliest Start (ES)
    es = [1] * (n + 1)
    temp_in = list(in_degree)
    
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if es[u] + 1 > es[v]:
                es[v] = es[u] + 1
            temp_in[v] -= 1
            if temp_in[v] == 0:
                q.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Compute Latest Start (LS)
    ls = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if ls[v] - 1 < ls[u]:
                ls[u] = ls[v] - 1

    for i in range(1, n + 1):
        if es[i] > ls[i] or es[i] > T or ls[i] < 1:
            print("NO")
            return

    # Interval capacity check
    for t1 in range(1, T + 1):
        for t2 in range(t1, T + 1):
            cnt = sum(1 for i in range(1, n + 1) if t1 <= es[i] and ls[i] <= t2)
            if cnt > M * (t2 - t1 + 1):
                print("NO")
                return

    # Count descendants for tie-breaking
    desc_count = [0] * (n + 1)
    for u in reversed(topo_order):
        desc = set()
        for v in adj[u]:
            desc.add(v)
            desc.update(adj[v])  # direct and some indirect
        desc_count[u] = len(desc)

    # Greedy heuristics / randomized list scheduling
    start_time = time.time()
    
    def try_greedy(randomize=False):
        deg = list(in_degree)
        cycle_assignment = [0] * (n + 1)
        ready = [i for i in range(1, n + 1) if deg[i] == 0]
        
        for t in range(1, T + 1):
            # Tasks that MUST be scheduled by time t
            must = []
            other = []
            for u in ready:
                if ls[u] <= t:
                    must.append(u)
                else:
                    other.append(u)
            
            if len(must) > M:
                return None
            
            if randomize:
                other.sort(key=lambda u: (ls[u], -desc_count[u], random.random()))
            else:
                other.sort(key=lambda u: (ls[u], -desc_count[u]))
            
            chosen = must + other[:M - len(must)]
            
            chosen_set = set(chosen)
            ready = [u for u in ready if u not in chosen_set]
            
            for u in chosen:
                cycle_assignment[u] = t
                for v in adj[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        ready.append(v)
                        
        if all(cycle_assignment[i] > 0 for i in range(1, n + 1)):
            return cycle_assignment
        return None

    # Try deterministic greedy
    res = try_greedy(randomize=False)
    if res is not None:
        print("YES")
        print(*(res[1:]))
        return

    # Try randomized greedy
    while time.time() - start_time < 1.5:
        res = try_greedy(randomize=True)
        if res is not None:
            print("YES")
            print(*(res[1:]))
            return

    # Backtracking search if greedy didn't find within time
    assignment = [0] * (n + 1)
    
    def backtrack(t, current_ready, current_in_degree):
        if t > T:
            return all(assignment[i] > 0 for i in range(1, n + 1))
        
        # Check unready tasks that have ls[v] <= t
        for i in range(1, n + 1):
            if assignment[i] == 0 and ls[i] <= t and i not in current_ready:
                return False

        must = []
        other = []
        for u in current_ready:
            if ls[u] <= t:
                must.append(u)
            else:
                other.append(u)

        if len(must) > M:
            return False

        other.sort(key=lambda u: (ls[u], -desc_count[u]))
        rem_slots = M - len(must)

        # Generate candidate subsets from other
        # Prioritize taking as many top elements as possible
        from itertools import combinations
        max_take = min(rem_slots, len(other))
        
        for k in range(max_take, -1, -1):
            for extra in combinations(other[:max_take + 2], k):
                chosen = must + list(extra)
                
                # Apply choices
                next_ready = [u for u in current_ready if u not in chosen]
                new_in_degree = list(current_in_degree)
                for u in chosen:
                    assignment[u] = t
                    for v in adj[u]:
                        new_in_degree[v] -= 1
                        if new_in_degree[v] == 0:
                            next_ready.append(v)

                if backtrack(t + 1, next_ready, new_in_degree):
                    return True

                # Undo
                for u in chosen:
                    assignment[u] = 0

                if time.time() - start_time > 4.5:
                    return False
        return False

    init_ready = [i for i in range(1, n + 1) if in_degree[i] == 0]
    if backtrack(1, init_ready, list(in_degree)):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()