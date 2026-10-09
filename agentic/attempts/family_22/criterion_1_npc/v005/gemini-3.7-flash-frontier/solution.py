import sys
from collections import deque
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    M = int(next(iterator))
    T = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        radj[v].append(u)
        in_degree[v] += 1
        
    # Check for cycles and compute topological sort
    q = deque([i for i in range(n) if in_degree[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if len(topo) < n:
        print("NO")
        return

    # Compute ES (earliest slot)
    es = [1] * n
    for u in topo:
        for v in adj[u]:
            if es[u] + 1 > es[v]:
                es[v] = es[u] + 1

    # Compute LS (latest slot)
    ls = [T] * n
    for u in reversed(topo):
        for v in adj[u]:
            if ls[v] - 1 < ls[u]:
                ls[u] = ls[v] - 1

    for i in range(n):
        if es[i] > ls[i]:
            print("NO")
            return

    # Predecessor masks
    pred_mask = [0] * n
    for u in topo:
        mask = 0
        for p in radj[u]:
            mask |= (1 << p) | pred_mask[p]
        pred_mask[u] = mask

    # Successor counts/depths for tie-breaking
    desc_count = [0] * n
    succ_mask = [0] * n
    for u in reversed(topo):
        mask = 0
        for s in adj[u]:
            mask |= (1 << s) | succ_mask[s]
        succ_mask[u] = mask
        desc_count[u] = bin(mask).count('1')

    # Slot assignment result
    ans_slot = [0] * n

    all_done = (1 << n) - 1
    memo = set()

    def search(slot, done_mask):
        if done_mask == all_done:
            return True
        if slot > T:
            return False

        state = (slot, done_mask)
        if state in memo:
            return False

        # Available jobs
        available = []
        must_schedule = []
        for i in range(n):
            if not (done_mask & (1 << i)):
                if (pred_mask[i] & done_mask) == pred_mask[i]:
                    available.append(i)
                    if ls[i] == slot:
                        must_schedule.append(i)
                else:
                    if ls[i] <= slot:
                        # Job i cannot be done in time
                        memo.add(state)
                        return False

        if len(must_schedule) > M:
            memo.add(state)
            return False

        # Sort available jobs: those with smaller LS, then larger desc_count first
        available.sort(key=lambda x: (ls[x], -desc_count[x]))

        must_set = set(must_schedule)
        optional = [x for x in available if x not in must_set]
        k = M - len(must_schedule)

        # Generate candidate subsets
        if len(optional) <= k:
            candidate_combos = [must_schedule + optional]
        else:
            # We must pick k from optional
            # Prioritize picking elements from the front of optional
            candidate_combos = [must_schedule + list(comb) for comb in combinations(optional, k)]

        for choice in candidate_combos:
            next_mask = done_mask
            for job in choice:
                next_mask |= (1 << job)
                ans_slot[job] = slot

            if search(slot + 1, next_mask):
                return True

        memo.add(state)
        return False

    if search(1, 0):
        print("YES")
        print(*(ans_slot[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()