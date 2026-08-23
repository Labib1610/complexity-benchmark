import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    def dfs(u, c):
        color[u] = c
        for v in adj[u]:
            if color[v] == 0:
                if not dfs(v, 3 - c):
                    return False
            elif color[v] == c:
                return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
    
    print("YES")
    print(*color[1:])

if __name__ == "__main__":
    threading.Thread(target=main).start()