import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    conflicts = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        conflicts[u].append(v)
        conflicts[v].append(u)
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for bank in (1, 2, 3):
            ok = True
            for nb in conflicts[idx]:
                if assignment[nb] == bank:
                    ok = False
                    break
            if ok:
                assignment[idx] = bank
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()