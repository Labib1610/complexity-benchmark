import sys
input = sys.stdin.readline

def solve():
    q = int(input())
    t = int(input())
    
    n = 3 * q
    
    # Read all schematics
    schematics = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        schematics.append((a, b, c))
    
    # Build adjacency: for each pair (u,v), store the third gear and schematic index
    pair_to_third = {}
    pair_to_idx = {}
    for idx, (a, b, c) in enumerate(schematics):
        pairs = [(a, b, c), (a, c, b), (b, c, a)]
        for x, y, z in pairs:
            if x > y:
                x, y = y, x
            pair_to_third[(x, y)] = z
            pair_to_idx[(x, y)] = idx
    
    # Build adjacency list for each gear
    adj = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(schematics):
        adj[a].append((b, c, idx))
        adj[b].append((a, c, idx))
        adj[c].append((a, b, idx))
    
    used = [False] * (n + 1)
    used_schematic = [False] * t
    result = []
    
    # Greedy approach: process gears in order, find matching schematic
    for gear in range(1, n + 1):
        if used[gear]:
            continue
        
        # Find a schematic containing this gear with two unused gears
        found = False
        for b, c, idx in adj[gear]:
            if not used[b] and not used[c] and not used_schematic[idx]:
                used[gear] = True
                used[b] = True
                used[c] = True
                used_schematic[idx] = True
                result.append((gear, b, c))
                found = True
                break
        
        if not found:
            print("NO")
            return
    
    print("YES")
    for a, b, c in result:
        print(a, b, c)

solve()