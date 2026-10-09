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
        
    color = [0] * (n + 1)
    camp = [[], []]
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                camp[color[u] - 1].append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                        
    if len(camp[0]) >= k:
        print("YES")
        print(" ".join(map(str, camp[0][:k])))
    elif len(camp[1]) >= k:
        print("YES")
        print(" ".join(map(str, camp[1][:k])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()