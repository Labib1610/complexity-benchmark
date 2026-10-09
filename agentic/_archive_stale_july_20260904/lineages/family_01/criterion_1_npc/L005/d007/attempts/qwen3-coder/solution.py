from collections import defaultdict
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def interference(pu, pv):
    return pu * pu + pu * pv + pv * pv

def is_valid(pu, pv):
    return interference(pu, pv) % 3 != 0

# Precompute valid pairs
valid_pairs = set()
for p1 in [1, 2, 3]:
    for p2 in [1, 2, 3]:
        if is_valid(p1, p2):
            valid_pairs.add((p1, p2))

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print("1 " * n)
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all 3^n combinations, but in a smart way using backtracking
    # and prioritizing to minimize V_n
    
    best_config = None
    min_potential = None
    
    def compute_potential(config):
        if not config:
            return 0
        V = config[0]
        for i in range(1, len(config)):
            V = 4 * V + config[i]
        return V
    
    def is_consistent(config):
        # Check if current partial assignment is consistent
        idx = len(config) - 1
        for neighbor in adj[idx]:
            if neighbor < len(config):
                if not is_valid(config[idx], config[neighbor]):
                    return False
        return True
    
    def backtrack(config):
        nonlocal best_config, min_potential
        
        if len(config) == n:
            potential = compute_potential(config)
            if min_potential is None or potential < min_potential:
                min_potential = potential
                best_config = config[:]
            return
        
        # Try frequencies in order 1, 2, 3 to minimize potential
        for freq in [1, 2, 3]:
            config.append(freq)
            if is_consistent(config):
                # Prune if current path cannot lead to better solution
                if min_potential is not None:
                    current_potential = compute_potential(config)
                    # Estimate minimum possible extension
                    remaining = n - len(config)
                    min_extension = sum(1 * (4 ** i) for i in range(remaining))
                    estimated_min = current_potential * (4 ** remaining) + min_extension
                    if estimated_min >= min_potential:
                        config.pop()
                        continue
                
                backtrack(config)
            config.pop()
    
    backtrack([])
    
    if best_config is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best_config)))

solve()