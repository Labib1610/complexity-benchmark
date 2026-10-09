import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))  # 0-index for bitmasking
    
    # Sort for better pruning
    triples.sort()
    
    used_x = [False]*k
    used_y = [False]*k
    used_z = [False]*k
    
    chosen = []
    
    # Precompute for pruning: for each index, list of triples that can still be used
    # We'll just do simple recursion with pruning by counting available triples
    
    def backtrack(start, count):
        if count == k:
            return True
        # Prune: if not enough triples left
        remaining = 0
        for i in range(start, t):
            x, y, z = triples[i]
            if not used_x[x] and not used_y[y] and not used_z[z]:
                remaining += 1
        if remaining < k - count:
            return False
        
        for i in range(start, t):
            x, y, z = triples[i]
            if not used_x[x] and not used_y[y] and not used_z[z]:
                # choose
                used_x[x] = used_y[y] = used_z[z] = True
                chosen.append((x+1, y+1, z+1))
                if backtrack(i+1, count+1):
                    return True
                # backtrack
                chosen.pop()
                used_x[x] = used_y[y] = used_z[z] = False
        return False
    
    if backtrack(0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()