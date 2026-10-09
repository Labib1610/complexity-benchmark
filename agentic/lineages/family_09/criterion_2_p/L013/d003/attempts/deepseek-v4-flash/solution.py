import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    color = [-1] * n
    color_count = [0, 0]
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            color_count[0] += 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        color_count[color[v]] += 1
                        stack.append(v)
    
    if color_count[0] >= k:
        chosen = [i+1 for i in range(n) if color[i] == 0][:k]
    elif color_count[1] >= k:
        chosen = [i+1 for i in range(n) if color[i] == 1][:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(map(str, chosen)))

if __name__ == "__main__":
    solve()