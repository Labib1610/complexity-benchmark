import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    iterator = iter(data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    n = 3 * q
    
    # Build adjacency list: for each person, list of tuples (unit_idx, p2, p3)
    # where the unit is (person, p2, p3) with person < p2 < p3
    adj = [[] for _ in range(n + 1)]
    
    units = []
    for i in range(t):
        try:
            a = int(next(iterator))
            b = int(next(iterator))
            c = int(next(iterator))
        except StopIteration:
            break
        
        # The input guarantees a < b < c
        units.append((a, b, c))
        adj[a].append((i, b, c))
        adj[b].append((i, a, c))
        adj[c].append((i, a, b))

    # We need to select q units covering all n persons exactly once.
    # This is an Exact Cover problem.
    # Given constraints q <= 200, n <= 600, t <= 20000.
    # We use backtracking with heuristics.
    
    used = [False] * (n + 1)
    selected_units = []
    
    # Pre-calculate unit members for quick access
    unit_members = [set(u) for u in units]
    
    # Optimization: order persons by degree (number of units they belong to)
    # to fail faster. Persons with fewer options should be assigned first.
    person_order = list(range(1, n + 1))
    person_order.sort(key=lambda p: len(adj[p]))
    
    def backtrack(k):
        # k is the number of units selected so far
        if k == q:
            return True
        
        # Find the next unassigned person
        # We follow the heuristic order
        p = -1
        for person in person_order:
            if not used[person]:
                p = person
                break
        
        if p == -1:
            return False # Should not happen if logic is correct
            
        # Try all units containing p
        for u_idx, m2, m3 in adj[p]:
            if not used[m2] and not used[m3]:
                # Check if unit is valid (all members free)
                # Note: p is already known to be free
                
                # Select unit
                used[p] = True
                used[m2] = True
                used[m3] = True
                selected_units.append(u_idx)
                
                if backtrack(k + 1):
                    return True
                
                # Backtrack
                selected_units.pop()
                used[p] = False
                used[m2] = False
                used[m3] = False
                
        return False

    if backtrack(0):
        print("YES")
        for u_idx in selected_units:
            a, b, c = units[u_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()