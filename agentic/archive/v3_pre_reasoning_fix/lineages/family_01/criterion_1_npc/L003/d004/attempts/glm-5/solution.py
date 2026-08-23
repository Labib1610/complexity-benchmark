import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
    adj = [list(s) for s in adj]
    
    color = [0] * n
    avail = [7] * n  # bits 0,1,2 for colors 1,2,3
    
    def backtrack(i):
        if i == n:
            return True
        for c in range(3):
            bit = 1 << c
            if not (avail[i] & bit):
                continue
            color[i] = c + 1
            removed = []
            valid = True
            for j in adj[i]:
                if color[j] == 0 and (avail[j] & bit):
                    avail[j] &= ~bit
                    removed.append(j)
                    if avail[j] == 0:
                        valid = False
                        break
            if valid:
                if backtrack(i + 1):
                    return True
            for j in removed:
                avail[j] |= bit
            color[i] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()