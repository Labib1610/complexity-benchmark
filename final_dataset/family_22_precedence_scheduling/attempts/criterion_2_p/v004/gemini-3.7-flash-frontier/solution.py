import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        in_degree[v] += 1
        idx += 2
        
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(order) == n:
        print("YES")
        print(*(order))
    else:
        print("NO")

if __name__ == '__main__':
    main()