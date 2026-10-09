import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[x-1].append((y-1, z-1))
    
    # Sort to have deterministic order
    for i in range(k):
        allowed[i].sort()
    
    used_app = [False] * k
    used_shift = [False] * k
    chosen = [None] * k
    
    # Memoization: state = (operator_index, apparatus_mask, shift_mask)
    from functools import lru_cache
    
    @lru_cache(None)
    def dfs(op_idx, app_mask, shift_mask):
        if op_idx == k:
            return True
        for y, z in allowed[op_idx]:
            if not (app_mask >> y) & 1 and not (shift_mask >> z) & 1:
                chosen[op_idx] = (op_idx+1, y+1, z+1)
                if dfs(op_idx+1, app_mask | (1 << y), shift_mask | (1 << z)):
                    return True
        return False
    
    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()