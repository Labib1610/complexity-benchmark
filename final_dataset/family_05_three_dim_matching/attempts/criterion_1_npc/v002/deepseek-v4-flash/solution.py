import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = set()
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed.add((x - 1, y - 1, z - 1))
    
    # We'll try to match appetizers to (main, dessert) pairs
    # Use backtracking with pruning
    
    # For each appetizer, list possible (y,z) pairs
    options = [[] for _ in range(k)]
    for x, y, z in allowed:
        options[x].append((y, z))
    
    # Sort options by size for better pruning
    for i in range(k):
        options[i].sort(key=lambda p: (p[0], p[1]))
    
    used_y = [False] * k
    used_z = [False] * k
    assignment = [None] * k  # assignment[x] = (y, z)
    
    # Precompute for each appetizer the possible y,z sets
    # We'll do backtracking over appetizers
    
    def backtrack(x):
        if x == k:
            return True
        for y, z in options[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                assignment[x] = (y, z)
                if backtrack(x + 1):
                    return True
                used_y[y] = False
                used_z[z] = False
                assignment[x] = None
        return False
    
    if backtrack(0):
        print("YES")
        for x in range(k):
            y, z = assignment[x]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()