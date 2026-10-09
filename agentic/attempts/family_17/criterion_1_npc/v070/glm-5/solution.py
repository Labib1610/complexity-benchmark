import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    squads = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        squads.append((a, b, c))
    
    n = 3 * q
    
    # Build adjacency list: for each person, list of squad indices they belong to
    person_to_squads = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(squads):
        person_to_squads[a].append(idx)
        person_to_squads[b].append(idx)
        person_to_squads[c].append(idx)
    
    # State: which squads are selected, which persons are used
    selected = []
    used = [False] * (n + 1)
    
    # For efficiency, track which squads are still available
    squad_available = [True] * t
    
    def backtrack(pos):
        if len(selected) == q:
            return True
        
        # Find the smallest unused person
        start_person = 1
        while start_person <= n and used[start_person]:
            start_person += 1
        
        if start_person > n:
            return False
        
        # Try each squad containing this person
        for squad_idx in person_to_squads[start_person]:
            if not squad_available[squad_idx]:
                continue
            a, b, c = squads[squad_idx]
            if used[a] or used[b] or used[c]:
                continue
            
            # Select this squad
            selected.append(squad_idx)
            used[a] = used[b] = used[c] = True
            squad_available[squad_idx] = False
            
            if backtrack(pos + 1):
                return True
            
            # Backtrack
            selected.pop()
            used[a] = used[b] = used[c] = False
            squad_available[squad_idx] = True
        
        return False
    
    if backtrack(0):
        print("YES")
        for idx in selected:
            a, b, c = squads[idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()