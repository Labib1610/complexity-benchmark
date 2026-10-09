import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    profiles = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        profiles.append((x-1, y-1, z-1))
    
    # Group profiles by operator
    by_op = [[] for _ in range(k)]
    for x, y, z in profiles:
        by_op[x].append((y, z))
    
    # Sort each list to have deterministic order
    for i in range(k):
        by_op[i].sort()
    
    # Backtracking with memoization
    memo = {}
    chosen = [None] * k
    
    def dfs(op_idx, term_mask, shift_mask):
        if op_idx == k:
            return True
        key = (op_idx, term_mask, shift_mask)
        if key in memo:
            return memo[key]
        for y, z in by_op[op_idx]:
            if not (term_mask >> y) & 1 and not (shift_mask >> z) & 1:
                chosen[op_idx] = (op_idx, y, z)
                if dfs(op_idx + 1, term_mask | (1 << y), shift_mask | (1 << z)):
                    memo[key] = True
                    return True
        memo[key] = False
        return False
    
    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()