import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to find assignment x_i in {1, 2} such that for each edge (u, v):
    # x_u + x_v is odd.
    # This is a bipartite graph check (2-coloring).
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS
            queue = [i]
            color[i] = 1
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        # Lexicographically smallest: prefer 1 over 2.
        # color[u] = 1 -> x_u = 1
        # color[u] = 2 -> x_u = 2
        print(*(color[i] for i in range(1, n + 1)))

if __name__ == '__main__':
    solve()