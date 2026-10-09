import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    iterator = iter(input)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Colors: 1 or 2
    color = [0] * n
    
    # BFS queue
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()