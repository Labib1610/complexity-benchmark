import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        in_deg[v] += 1
        idx += 2
        
    queue = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
                
    if len(order) == n:
        sys.stdout.write("YES\n" + " ".join(map(str, order)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    main()