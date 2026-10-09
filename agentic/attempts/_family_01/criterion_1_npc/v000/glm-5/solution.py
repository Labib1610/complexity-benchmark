import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    for i in range(m):
        u = int(input_data[2 + 2 * i]) - 1
        v = int(input_data[3 + 2 * i]) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        
    color = [0] * n
    ALL = (1 << n) - 1
    
    def dfs(u, c):
        color[u] = c
        mask = 1 << u
        for v in range(n):
            if adj[u] & (1 << v):
                if color[v] == c:
                    return False
                if color[v] == 0:
                    if not dfs(v, 3 - c):
                        return False
        return True

    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return

    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1, 1 << n):
        v = (mask & -mask).bit_length() - 1
        prev = mask ^ (1 << v)
        if dp[prev] and (adj[v] & prev) == 0:
            dp[mask] = 1
            
    for mask in range(1 << n):
        if dp[mask] and dp[mask ^ ALL]:
            res = [0] * n
            for i in range(n):
                if mask & (1 << i):
                    res[i] = 1
                else:
                    res[i] = 2
            for i in range(n):
                if color[i] == 2:
                    res[i] = 3
            print("YES")
            print(" ".join(map(str, res)))
            return
            
    print("NO")

if __name__ == '__main__':
    solve()