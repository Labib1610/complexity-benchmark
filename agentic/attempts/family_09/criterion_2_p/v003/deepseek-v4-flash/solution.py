import sys

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    group0 = []
    group1 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            group0.append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        if color[v] == 0:
                            group0.append(v)
                        else:
                            group1.append(v)
                        stack.append(v)
    
    if len(group0) >= k:
        ans = group0[:k]
    elif len(group1) >= k:
        ans = group1[:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x + 1) for x in ans))

if __name__ == "__main__":
    main()