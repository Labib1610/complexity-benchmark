import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    incompatible = [set() for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        incompatible[u].add(v)
        incompatible[v].add(u)
    
    assignment = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        
        forbidden = 0
        for j in range(i):
            if j in incompatible[i]:
                forbidden |= (1 << assignment[j])
        
        for g in range(1, 4):
            if not (forbidden & (1 << g)):
                assignment[i] = g
                if backtrack(i + 1):
                    return True
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

solve()