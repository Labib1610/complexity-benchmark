import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    it = iter(input)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # State array: 0 = unvisited, 1 = state 1, 2 = state 2
    state = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if state[i] == 0:
            # BFS for this component
            # Try to assign state 1 to i (lexicographically smallest choice)
            queue = deque([i])
            state[i] = 1
            possible = True
            
            while queue:
                u = queue.popleft()
                su = state[u]
                # The neighbor must have state 3 - su
                sv = 3 - su
                for v in adj[u]:
                    if state[v] == 0:
                        state[v] = sv
                        queue.append(v)
                    elif state[v] != sv:
                        possible = False
                        # We can break early, but need to drain queue or use a flag
                        # Setting a flag and breaking inner loop
                        break
                if not possible:
                    break
            
            if not possible:
                print("NO")
                return
    
    print("YES")
    print(*(state[1:]))

if __name__ == "__main__":
    solve()