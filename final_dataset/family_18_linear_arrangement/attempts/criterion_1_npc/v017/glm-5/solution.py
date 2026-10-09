import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    if n == 0:
        print("YES")
        print()
        return
    
    if n == 1:
        if 0 <= B:
            print("YES")
            print(1)
        else:
            print("NO")
        return
    
    best_cost = float('inf')
    best_perm = None
    
    if n <= 11:
        for perm in permutations(range(1, n+1)):
            pos = [0] * (n + 1)
            for i, mod in enumerate(perm):
                pos[mod] = i + 1
            cost = 0
            for u in range(1, n+1):
                for v in adj[u]:
                    if v > u:
                        cost += abs(pos[u] - pos[v])
            if cost < best_cost:
                best_cost = cost
                best_perm = list(perm)
                if cost <= B:
                    break
    elif n <= 16:
        # Branch and bound
        best_cost = float('inf')
        best_perm = None
        
        def dfs(placed, positions, used, cost):
            nonlocal best_cost, best_perm
            if cost >= best_cost:
                return
            if len(placed) == n:
                if cost < best_cost:
                    best_cost = cost
                    best_perm = placed[:]
                return
            
            pos_idx = len(placed) + 1
            
            # Lower bound: remaining edges contribute at least 1 each
            remaining_edges = 0
            for u in range(1, n+1):
                if positions[u] == 0:
                    for v in adj[u]:
                        if v > u and positions[v] == 0:
                            remaining_edges += 1
            if cost + remaining_edges >= best_cost:
                return
            
            # Try placing modules at this position
            for mod in range(1, n+1):
                if not used[mod]:
                    new_cost = cost
                    for nb in adj[mod]:
                        if positions[nb] != 0:
                            new_cost += abs(pos_idx - positions[nb])
                    if new_cost < best_cost:
                        positions[mod] = pos_idx
                        used[mod] = True
                        placed.append(mod)
                        dfs(placed, positions, used, new_cost)
                        placed.pop()
                        used[mod] = False
                        positions[mod] = 0
        
        positions = [0] * (n + 1)
        used = [False] * (n + 1)
        dfs([], positions, used, 0)
    else:
        # Greedy heuristic for large n
        degrees = [(len(adj[i]), i) for i in range(1, n+1)]
        degrees.sort(reverse=True)
        
        perm = [0] * n
        center = (n + 1) // 2
        left = center - 1
        right = center
        
        placed = set()
        queue = []
        
        # Place highest degree module at center
        top_mod = degrees[0][1]
        if n % 2 == 1:
            perm[center - 1] = top_mod
            placed.add(top_mod)
            left = center - 2
            right = center
        else:
            perm[center - 1] = top_mod
            placed.add(top_mod)
            left = center - 2
            right = center
        
        # Add neighbors to queue
        for nb in adj[top_mod]:
            if nb not in placed:
                queue.append((len(adj[nb]), nb))
        queue.sort(reverse=True)
        
        while queue and (left >= 0 or right < n):
            _, mod = queue.pop(0)
            if mod in placed:
                continue
            if right < n:
                perm[right] = mod
                placed.add(mod)
                right += 1
            elif left >= 0:
                perm[left] = mod
                placed.add(mod)
                left -= 1
            for nb in adj[mod]:
                if nb not in placed:
                    queue.append((len(adj[nb]), nb))
            queue.sort(reverse=True)
        
        # Fill remaining
        for i in range(n):
            if perm[i] == 0:
                for mod in range(1, n+1):
                    if mod not in placed:
                        perm[i] = mod
                        placed.add(mod)
                        break
        
        best_perm = perm
        pos = [0] * (n + 1)
        for i, mod in enumerate(best_perm):
            pos[mod] = i + 1
        best_cost = 0
        for u in range(1, n+1):
            for v in adj[u]:
                if v > u:
                    best_cost += abs(pos[u] - pos[v])
    
    if best_cost <= B:
        print("YES")
        print(' '.join(map(str, best_perm)))
    else:
        print("NO")

solve()