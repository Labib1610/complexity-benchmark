import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [-1] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            comp = [[], []]
            stack = [i]
            color[i] = 0
            comp[0].append(i)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        comp[color[v]].append(v)
                        stack.append(v)
            components.append(comp)
            
    dp = [[False] * (k + 1) for _ in range(len(components) + 1)]
    dp[0][0] = True
    
    for i in range(1, len(components) + 1):
        c0 = len(components[i-1][0])
        c1 = len(components[i-1][1])
        for j in range(k + 1):
            if dp[i-1][j]:
                if j + c0 <= k:
                    dp[i][j + c0] = True
                if j + c1 <= k:
                    dp[i][j + c1] = True
                    
    if not dp[len(components)][k]:
        print("NO")
        return
        
    print("YES")
    
    choices = [0] * (len(components) + 1)
    curr = k
    for i in range(len(components), 0, -1):
        c0 = len(components[i-1][0])
        c1 = len(components[i-1][1])
        if curr >= c0 and dp[i-1][curr - c0]:
            choices[i] = 0
            curr -= c0
        else:
            choices[i] = 1
            curr -= c1
            
    ans = []
    for i in range(1, len(components) + 1):
        ans.extend(components[i-1][choices[i]])
        
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()