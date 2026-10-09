import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[False] * n for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u][v] = True
        adj[v][u] = True
        
    assignment = [0] * n
    
    def dfs(u):
        for c in range(1, 4):
            valid = True
            for v in range(u):
                if adj[u][v] and assignment[v] == c:
                    valid = False
                    break
            if valid:
                assignment[u] = c
                if u == n - 1 or dfs(u + 1):
                    return True
        assignment[u] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()