import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    profiles = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        profiles.append((x-1, y-1, z-1))
    
    # Group profiles by operator for faster lookup
    by_operator = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(profiles):
        by_operator[x].append((y, z, idx))
    
    used_terminal = 0
    used_shift = 0
    chosen = []
    
    # Precompute for pruning: for each operator, list of (terminal, shift) pairs
    # We'll do DFS over operators 0..k-1
    
    def dfs(op):
        nonlocal used_terminal, used_shift
        if op == k:
            return True
        for y, z, idx in by_operator[op]:
            if not (used_terminal >> y) & 1 and not (used_shift >> z) & 1:
                used_terminal |= (1 << y)
                used_shift |= (1 << z)
                chosen.append(profiles[idx])
                if dfs(op + 1):
                    return True
                chosen.pop()
                used_terminal ^= (1 << y)
                used_shift ^= (1 << z)
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()