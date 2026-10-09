import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # State: 0 = unvisited, 1 = mode 1, 2 = mode 2
    state = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if state[i] == 0:
            # BFS queue
            queue = [i]
            state[i] = 1
            
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                
                for v in adj[u]:
                    if state[v] == 0:
                        state[v] = 3 - state[u]
                        queue.append(v)
                    elif state[v] == state[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(state[1:]))

if __name__ == '__main__':
    solve()