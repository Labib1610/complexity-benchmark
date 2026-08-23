import sys
import collections

# Set recursion limit higher just in case, though we use iterative BFS.
sys.setrecursionlimit(1 << 25)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Configuration array: 0=unassigned, 1 or 2 assigned.
    # We aim for lexicographically smallest, so we prefer assigning 1.
    config = [0] * (n + 1)
    
    # Queue for BFS
    queue = collections.deque()
    
    possible = True
    
    for i in range(1, n + 1):
        if config[i] == 0:
            # Start a new connected component
            config[i] = 1
            queue.append(i)
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if config[v] == 0:
                        config[v] = 3 - config[u]
                        queue.append(v)
                    elif config[v] == config[u]:
                        possible = False
                        # We can break early, but need to consume input or just exit
                        # Since we read all input, just set flag and break loops
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        # Output configurations for relays 1 to n
        print(*(config[1:n+1]))

if __name__ == '__main__':
    solve()