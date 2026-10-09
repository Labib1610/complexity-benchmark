import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    relays = []
    by_a = [[] for _ in range(k+1)]
    for _ in range(t):
        a,b,c = map(int, input().split())
        relays.append((a,b,c))
        by_a[a].append((b,c))
    
    used_b = [False]*(k+1)
    used_c = [False]*(k+1)
    chosen = [None]*(k+1)
    
    def dfs(a):
        if a > k:
            return True
        for b,c in by_a[a]:
            if not used_b[b] and not used_c[c]:
                used_b[b] = True
                used_c[c] = True
                chosen[a] = (a,b,c)
                if dfs(a+1):
                    return True
                used_b[b] = False
                used_c[c] = False
        return False
    
    if dfs(1):
        print("YES")
        for a in range(1,k+1):
            print(*chosen[a])
    else:
        print("NO")

if __name__ == "__main__":
    solve()