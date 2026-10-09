import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    combos = []
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        combos.append((p1-1, p2-1, p3-1))
    
    # Group by tower
    by_tower = [[] for _ in range(k)]
    for a, b, c in combos:
        by_tower[a].append((b, c))
    
    # Sort each list for deterministic order
    for i in range(k):
        by_tower[i].sort()
    
    used_keys = 0
    used_links = 0
    chosen = [None] * k
    
    # Precompute for each tower, list of (key, link) pairs
    # Backtracking over towers
    def dfs(tower_idx):
        nonlocal used_keys, used_links
        if tower_idx == k:
            return True
        for key, link in by_tower[tower_idx]:
            if not (used_keys & (1 << key)) and not (used_links & (1 << link)):
                used_keys |= (1 << key)
                used_links |= (1 << link)
                chosen[tower_idx] = (tower_idx+1, key+1, link+1)
                if dfs(tower_idx + 1):
                    return True
                used_keys ^= (1 << key)
                used_links ^= (1 << link)
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()