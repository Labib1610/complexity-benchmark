import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(data[2 + 2 * i])
        v = int(data[3 + 2 * i])
        adj[u].append(v)
        adj[v].append(u)
        
    h = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if h[i] == 0:
            h[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if h[v] == 0:
                        h[v] = 3 - h[u]
                        stack.append(v)
                    elif h[v] == h[u]:
                        sys.stdout.write("NO\n")
                        return
                        
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, h[1:])) + "\n")

if __name__ == '__main__':
    solve()