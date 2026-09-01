import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    colors = [0] * n
    
    def is_safe(u, c):
        for v in adj[u]:
            if colors[v] == c:
                return False
        return True
        
    def backtrack(u):
        if u == n:
            return True
        for c in range(1, 4):
            if is_safe(u, c):
                colors[u] = c
                if backtrack(u + 1):
                    return True
                colors[u] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()