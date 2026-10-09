import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    def backtrack(node):
        if node == n:
            return True
        for c in range(1, 4):
            ok = True
            for nb in adj[node]:
                if nb < node and color[nb] == c:
                    ok = False
                    break
            if ok:
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()