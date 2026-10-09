import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    n = 3 * q
    
    # Build adjacency list for each person
    adj = [[] for _ in range(n + 1)]
    teams = []
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        teams.append((a, b, c))
        adj[a].append((b, c))
        adj[b].append((a, c))
        adj[c].append((a, b))
    
    # Sort adjacency lists for deterministic behavior
    for i in range(1, n + 1):
        adj[i].sort()
    
    used = [False] * (n + 1)
    result = []
    
    # Process in order of badge numbers
    for i in range(1, n + 1):
        if used[i]:
            continue
        
        # Find a valid team containing i
        found = False
        for b, c in adj[i]:
            if not used[b] and not used[c]:
                # Check if this team exists in the catalog
                # Since we built adj from teams, it does
                used[i] = True
                used[b] = True
                used[c] = True
                result.append((i, b, c))
                found = True
                break
        
        if not found:
            print("NO")
            return
    
    print("YES")
    for team in result:
        print(team[0], team[1], team[2])

solve()