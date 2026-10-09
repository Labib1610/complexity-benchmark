import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    edges = []
    for _ in range(t):
        d, f, m = map(int, input().split())
        edges.append((d-1, f-1, m-1))
    
    # Group edges by demographic
    by_d = [[] for _ in range(k)]
    for idx, (d, f, m) in enumerate(edges):
        by_d[d].append(idx)
    
    used_f = [False]*k
    used_m = [False]*k
    chosen = [None]*k
    
    # Sort demographics by number of options (smallest first)
    order = sorted(range(k), key=lambda d: len(by_d[d]))
    
    def dfs(pos):
        if pos == k:
            return True
        d = order[pos]
        for eidx in by_d[d]:
            _, f, m = edges[eidx]
            if not used_f[f] and not used_m[m]:
                used_f[f] = True
                used_m[m] = True
                chosen[d] = (d+1, f+1, m+1)
                if dfs(pos+1):
                    return True
                used_f[f] = False
                used_m[m] = False
        return False
    
    if dfs(0):
        print("YES")
        for d in range(k):
            print(*chosen[d])
    else:
        print("NO")

if __name__ == "__main__":
    solve()