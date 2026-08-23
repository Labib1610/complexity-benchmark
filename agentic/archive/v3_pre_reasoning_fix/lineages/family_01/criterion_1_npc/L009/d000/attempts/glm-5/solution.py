def solve():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    conflicts = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        conflicts[u].add(v)
        conflicts[v].add(u)
    
    assignment = [-1] * n
    forbid_count = [[0, 0, 0] for _ in range(n)]
    forbidden = [0] * n
    
    def backtrack(i):
        if i == n:
            return True
        
        for shift in range(3):
            if forbid_count[i][shift] > 0:
                continue
            
            assignment[i] = shift + 1
            bit = 1 << shift
            
            for j in conflicts[i]:
                if j > i:
                    forbid_count[j][shift] += 1
                    if forbid_count[j][shift] == 1:
                        forbidden[j] |= bit
            
            valid = True
            for j in range(i + 1, n):
                if forbidden[j] == 7:
                    valid = False
                    break
            
            if valid and backtrack(i + 1):
                return True
            
            for j in conflicts[i]:
                if j > i:
                    forbid_count[j][shift] -= 1
                    if forbid_count[j][shift] == 0:
                        forbidden[j] ^= bit
            
            assignment[i] = -1
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()