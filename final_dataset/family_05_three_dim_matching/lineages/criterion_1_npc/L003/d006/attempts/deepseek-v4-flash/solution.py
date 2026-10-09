import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # Group components by x value
    by_x = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        by_x[x].append((x, y, z))
    
    # We need exactly one component for each x value 1..k
    # and y and z must each cover 1..k exactly once.
    
    used_y = [False]*(k+1)
    used_z = [False]*(k+1)
    chosen = [None]*(k+1)
    
    # Pre-check: each x must have at least one component
    for x in range(1, k+1):
        if not by_x[x]:
            print("NO")
            return
    
    def backtrack(x):
        if x == k+1:
            return True
        for comp in by_x[x]:
            _, y, z = comp
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen[x] = comp
                if backtrack(x+1):
                    return True
                used_y[y] = False
                used_z[z] = False
        return False
    
    if backtrack(1):
        print("YES")
        for x in range(1, k+1):
            print(*chosen[x])
    else:
        print("NO")

if __name__ == "__main__":
    solve()