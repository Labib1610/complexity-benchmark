import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    protocols = []
    for _ in range(t):
        m, c, f = map(int, input().split())
        protocols.append((m-1, c-1, f-1))
    
    # Group by material
    by_material = [[] for _ in range(k)]
    for m, c, f in protocols:
        by_material[m].append((c, f))
    
    # Sort materials by number of options (smallest first) for pruning
    order = sorted(range(k), key=lambda x: len(by_material[x]))
    
    used_c = [False] * k
    used_f = [False] * k
    chosen = [None] * k
    
    def dfs(idx):
        if idx == k:
            return True
        m = order[idx]
        for c, f in by_material[m]:
            if not used_c[c] and not used_f[f]:
                used_c[c] = True
                used_f[f] = True
                chosen[m] = (m, c, f)
                if dfs(idx + 1):
                    return True
                used_c[c] = False
                used_f[f] = False
        return False
    
    if dfs(0):
        print("YES")
        for m, c, f in chosen:
            print(m+1, c+1, f+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()