import sys
sys.setrecursionlimit(10000000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    allowed = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[x].append((y, z))
    
    # Sort allowed combinations for potentially better pruning
    for i in range(1, k + 1):
        allowed[i].sort()
    
    used_machine = 0
    used_slot = 0
    chosen = [None] * (k + 1)
    
    # DFS over specialists
    def dfs(spec):
        nonlocal used_machine, used_slot
        if spec > k:
            return True
        for y, z in allowed[spec]:
            if not (used_machine >> (y - 1)) & 1 and not (used_slot >> (z - 1)) & 1:
                used_machine |= (1 << (y - 1))
                used_slot |= (1 << (z - 1))
                chosen[spec] = (spec, y, z)
                if dfs(spec + 1):
                    return True
                used_machine ^= (1 << (y - 1))
                used_slot ^= (1 << (z - 1))
        return False
    
    if dfs(1):
        print("YES")
        for i in range(1, k + 1):
            print(*chosen[i])
    else:
        print("NO")

if __name__ == "__main__":
    solve()