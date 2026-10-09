import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # Precompute adjacency: for each (x,y) pair, list of z's
    by_xy = {}
    for x, y, z in triples:
        by_xy.setdefault((x, y), []).append(z)
    
    # We'll do backtracking over x, then y, then z
    used_x = [False]*k
    used_y = [False]*k
    used_z = [False]*k
    chosen = []
    
    # Sort triples for better pruning
    triples.sort(key=lambda t: (t[0], t[1], t[2]))
    
    def backtrack(idx):
        if idx == k:
            return True
        # Find first unused x
        for x in range(k):
            if not used_x[x]:
                break
        else:
            return False
        
        used_x[x] = True
        # Try all y for this x
        for y in range(k):
            if used_y[y]:
                continue
            # Check if there is any z available for (x,y)
            if (x, y) not in by_xy:
                continue
            for z in by_xy[(x, y)]:
                if used_z[z]:
                    continue
                used_y[y] = True
                used_z[z] = True
                chosen.append((x+1, y+1, z+1))
                if backtrack(idx+1):
                    return True
                chosen.pop()
                used_y[y] = False
                used_z[z] = False
        used_x[x] = False
        return False
    
    if backtrack(0):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()