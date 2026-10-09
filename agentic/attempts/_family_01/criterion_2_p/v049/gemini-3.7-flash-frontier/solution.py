import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    shift = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if shift[i] != 0:
            continue
        
        shift[i] = 1
        queue = deque([i])
        
        while queue:
            u = queue.popleft()
            curr_shift = shift[u]
            next_shift = 2 if curr_shift == 1 else 1
            
            for v in adj[u]:
                if shift[v] == 0:
                    shift[v] = next_shift
                    queue.append(v)
                elif shift[v] != next_shift:
                    print("NO")
                    return

    print("YES")
    print(*(shift[1:]))

if __name__ == '__main__':
    solve()