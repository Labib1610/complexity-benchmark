import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    routes_by_source = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        routes_by_source[x-1].append((x, y, z))
    
    used_trans = [False] * k
    used_dest = [False] * k
    chosen = []
    
    def dfs(src_idx):
        if src_idx == k:
            return True
        # Prune: if not enough unused transformers/destinations for remaining sources
        remaining = k - src_idx
        if sum(1 for v in used_trans if not v) < remaining:
            return False
        if sum(1 for v in used_dest if not v) < remaining:
            return False
        for route in routes_by_source[src_idx]:
            x, y, z = route
            if not used_trans[y-1] and not used_dest[z-1]:
                used_trans[y-1] = True
                used_dest[z-1] = True
                chosen.append(route)
                if dfs(src_idx + 1):
                    return True
                chosen.pop()
                used_trans[y-1] = False
                used_dest[z-1] = False
        return False
    
    if dfs(0):
        print("YES")
        for r in chosen:
            print(*r)
    else:
        print("NO")

if __name__ == "__main__":
    solve()