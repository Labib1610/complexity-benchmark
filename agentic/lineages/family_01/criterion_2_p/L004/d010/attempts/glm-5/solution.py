import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # 0: unvisited, 1: state 1, 2: state 2
    state = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if state[i] == 0:
            # BFS for lexicographically smallest assignment
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
        print(' '.join(str(state[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()