import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = defaultdict(set)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort modules by degree (descending)
    modules = list(range(1, n + 1))
    modules.sort(key=lambda x: -len(adj[x]))
    
    # Greedy placement: place high-degree modules at ends
    pos = [0] * (n + 1)
    left, right = 1, n
    for i, mod in enumerate(modules):
        if i % 2 == 0:
            pos[mod] = left
            left += 1
        else:
            pos[mod] = right
            right -= 1
    
    # Calculate total harness length
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n + 1)))
        return
    
    # Try alternative placements
    best_total = total
    best_pos = pos[:]
    
    # Try placing highest degree module at position 1, then greedy
    for first_pos in range(1, n + 1):
        pos = [0] * (n + 1)
        used = [False] * (n + 1)
        pos[modules[0]] = first_pos
        used[first_pos] = True
        
        # Place remaining modules greedily
        left, right = 1, n
        while used[left]:
            left += 1
        while used[right]:
            right -= 1
        
        for mod in modules[1:]:
            # Calculate cost for each position
            cost_left = 0
            cost_right = 0
            for neighbor in adj[mod]:
                if pos[neighbor] != 0:
                    cost_left += abs(left - pos[neighbor])
                    cost_right += abs(right - pos[neighbor])
            
            if cost_left <= cost_right:
                pos[mod] = left
                used[left] = True
                while left <= n and used[left]:
                    left += 1
            else:
                pos[mod] = right
                used[right] = True
                while right >= 1 and used[right]:
                    right -= 1
        
        total = 0
        for u in range(1, n + 1):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        
        if total <= B:
            print("YES")
            print(' '.join(str(pos[i]) for i in range(1, n + 1)))
            return
        
        if total < best_total:
            best_total = total
            best_pos = pos[:]
    
    # Try reverse order
    modules_rev = modules[::-1]
    for first_pos in range(1, n + 1):
        pos = [0] * (n + 1)
        used = [False] * (n + 1)
        pos[modules_rev[0]] = first_pos
        used[first_pos] = True
        
        left, right = 1, n
        while used[left]:
            left += 1
        while used[right]:
            right -= 1
        
        for mod in modules_rev[1:]:
            cost_left = 0
            cost_right = 0
            for neighbor in adj[mod]:
                if pos[neighbor] != 0:
                    cost_left += abs(left - pos[neighbor])
                    cost_right += abs(right - pos[neighbor])
            
            if cost_left <= cost_right:
                pos[mod] = left
                used[left] = True
                while left <= n and used[left]:
                    left += 1
            else:
                pos[mod] = right
                used[right] = True
                while right >= 1 and used[right]:
                    right -= 1
        
        total = 0
        for u in range(1, n + 1):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        
        if total <= B:
            print("YES")
            print(' '.join(str(pos[i]) for i in range(1, n + 1)))
            return
        
        if total < best_total:
            best_total = total
            best_pos = pos[:]
    
    # Try simple linear placement
    for perm in [list(range(1, n + 1)), list(range(n, 0, -1))]:
        pos = [0] * (n + 1)
        for i, mod in enumerate(modules):
            pos[mod] = perm[i]
        
        total = 0
        for u in range(1, n + 1):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        
        if total <= B:
            print("YES")
            print(' '.join(str(pos[i]) for i in range(1, n + 1)))
            return
        
        if total < best_total:
            best_total = total
            best_pos = pos[:]
    
    print("NO")

if __name__ == "__main__":
    solve()