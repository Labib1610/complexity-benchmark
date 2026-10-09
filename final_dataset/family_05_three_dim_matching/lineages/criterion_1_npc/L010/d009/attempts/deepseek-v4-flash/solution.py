import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    relays = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        relays.append((a, b, c))
    
    # Group relays by first coordinate
    by_a = [[] for _ in range(k+1)]
    for r in relays:
        by_a[r[0]].append(r)
    
    # If any first coordinate missing, impossible
    for i in range(1, k+1):
        if not by_a[i]:
            print("NO")
            return
    
    used_b = [False]*(k+1)
    used_c = [False]*(k+1)
    chosen = [None]*(k+1)
    
    def dfs(a):
        if a == k+1:
            return True
        for (x, b, c) in by_a[a]:
            if not used_b[b] and not used_c[c]:
                used_b[b] = True
                used_c[c] = True
                chosen[a] = (x, b, c)
                if dfs(a+1):
                    return True
                used_b[b] = False
                used_c[c] = False
        return False
    
    if dfs(1):
        print("YES")
        for a in range(1, k+1):
            print(*chosen[a])
    else:
        print("NO")

if __name__ == "__main__":
    solve()