import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(2 * q + 1)]
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    
    match = [0] * (2 * q + 1)
    result = []
    
    for u in range(1, q + 1):
        if match[u] != 0:
            continue
        
        queue = deque()
        queue.append(u)
        parent = {u: None}
        found = -1
        
        while queue and found == -1:
            curr = queue.popleft()
            for v in adj[curr]:
                if v in parent:
                    continue
                parent[v] = curr
                if match[v] == 0:
                    found = v
                    break
                else:
                    queue.append(match[v])
        
        if found == -1:
            print("NO")
            return
        
        path = []
        curr = found
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        
        for i in range(1, len(path), 2):
            u = path[i]
            v = path[i-1]
            match[u] = v
            match[v] = u
    
    for u in range(1, q + 1):
        if match[u] == 0:
            print("NO")
            return
    
    print("YES")
    for u in range(1, q + 1):
        print(u, match[u])

if __name__ == "__main__":
    solve()