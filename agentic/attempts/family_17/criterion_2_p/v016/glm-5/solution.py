import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(q + 1)]
    
    # Preallocate arrays for degree and pair
    deg = [0] * (q + 1)
    pair = [0] * (q + 1)
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        deg[a] += 1

    # Queue for leaf reduction (controllers with only 1 edge)
    dq = deque()
    for u in range(1, q + 1):
        if deg[u] == 1:
            dq.append(u)

    # Topological sort like reduction
    while dq:
        u = dq.popleft()
        # If already processed or no edges left, continue
        if deg[u] != 1:
            continue
        
        # Find the only remaining edge
        v = -1
        for b in adj[u]:
            if pair[b] == 0: # unpaired platform
                v = b
                break
        
        if v == -1:
            # Should not happen if graph is consistent, but implies failure
            print("NO")
            return

        # Match u and v
        pair[u] = v
        pair[v] = u
        
        # Remove edges involving v from neighbors of v
        # Neighbors of v are controllers u' such that (u', v) is an edge
        # For controllers, we decrement degree and check for leaf
        # Constraint condition gives u' in [v-2q+1, v-1]
        
        low = max(1, v - 2 * q + 1)
        high = min(q, v - 1)
        
        # Iterate through all possible controllers that could be connected to v
        # This is O(q) per platform in worst case
        # But since sum of degrees is small, we can optimize if adj was stored differently
        # Given constraints and time limit, let's check feasibility
        
        # We don't have reverse adjacency, so we must scan range
        # To avoid O(q^2), note that we only check u where deg[u] > 0
        # However, iterating range is unavoidable without reverse adj
        
        # Optimization: 
        # If we built reverse adjacency list `in_edges` where in_edges[v] = list of controllers`
        # Space O(t) which is fine.
        pass # This block is logic building, will use in_edges in final code

    # Placeholder for logic using topological sort
    # Need to re-implement with correct data structures
    
    # --- Re-implementing with reverse adjacency ---
    # Fill adj and in_edges
    return

def solve_actual():
    import sys
    from collections import deque
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))

    adj = [[] for _ in range(q + 1)]
    in_edges = [[] for _ in range(2 * q + 1)]
    
    deg = [0] * (q + 1)
    # pair array: since controllers are 1..q and platforms q+1..2q
    # we use size 2q+1
    pair = [0] * (2 * q + 1)
    
    for _ in range(t):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        in_edges[v].append(u)
        deg[u] += 1
        
    dq = deque()
    for u in range(1, q + 1):
        if deg[u] == 1:
            dq.append(u)
            
    processed = 0
    
    while dq:
        u = dq.popleft()
        if deg[u] != 1:
            continue
        
        # Find available platform
        v = -1
        for b in adj[u]:
            if pair[b] == 0:
                v = b
                break
        
        if v == -1:
            print("NO")
            return
            
        pair[u] = v
        pair[v] = u
        processed += 1
        
        # Process in_edges of v
        for u_prime in in_edges[v]:
            if u_prime != u:
                deg[u_prime] -= 1
                if deg[u_prime] == 1:
                    dq.append(u_prime)
                    
    if processed != q:
        print("NO")
        return
        
    print("YES")
    for u in range(1, q + 1):
        print(u, pair[u])

if __name__ == '__main__':
    solve_actual()