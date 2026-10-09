import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [-1] * n
    is_bipartite = True
    
    for i in range(n):
        if color[i] == -1:
            queue = [i]
            color[i] = 0
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
            
    if not is_bipartite:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(c + 1) for c in color))

if __name__ == '__main__':
    solve()