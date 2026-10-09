import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        
        # Start BFS from the lowest unvisited index
        color[i] = 1
        queue = [i]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            c = color[u]
            next_c = 2 if c == 1 else 1
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_c
                    queue.append(v)
                elif color[v] != next_c:
                    print("NO")
                    return
                    
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()