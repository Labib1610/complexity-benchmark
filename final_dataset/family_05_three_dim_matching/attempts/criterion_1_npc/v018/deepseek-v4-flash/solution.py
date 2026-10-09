import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples[x-1].append((y-1, z-1))
    
    # Sort triples for each specialist to try more constrained first
    for i in range(k):
        triples[i].sort(key=lambda p: (p[0], p[1]))
    
    used_machine = 0
    used_time = 0
    assignment = [None] * k
    
    # Precompute for each specialist the list of possible (machine, time) pairs
    # We'll do DFS with pruning
    
    def dfs(spec_idx):
        nonlocal used_machine, used_time
        if spec_idx == k:
            return True
        for m, tm in triples[spec_idx]:
            if not (used_machine >> m) & 1 and not (used_time >> tm) & 1:
                used_machine |= (1 << m)
                used_time |= (1 << tm)
                assignment[spec_idx] = (spec_idx+1, m+1, tm+1)
                if dfs(spec_idx + 1):
                    return True
                used_machine ^= (1 << m)
                used_time ^= (1 << tm)
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in assignment:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()