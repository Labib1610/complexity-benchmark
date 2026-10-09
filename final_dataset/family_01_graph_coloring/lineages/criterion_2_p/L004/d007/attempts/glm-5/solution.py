import sys
sys.setrecursionlimit(1 << 25)

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

    # We need to assign s[i] in {1, 2} such that for every edge (u, v),
    # s[u] != s[v].
    # This is a bipartite graph check.
    # To find the lexicographically smallest valid assignment,
    # we use a greedy approach: iterate i from 1 to n, assign s[i] = 1 if possible,
    # else s[i] = 2. If neither is possible, it's impossible.
    
    s = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Check if we can assign 1 to i
        can_be_1 = True
        for neighbor in adj[i]:
            if s[neighbor] == 1:
                can_be_1 = False
                break
        
        if can_be_1:
            s[i] = 1
        else:
            # Check if we can assign 2 to i
            can_be_2 = True
            for neighbor in adj[i]:
                if s[neighbor] == 2:
                    can_be_2 = False
                    break
            
            if can_be_2:
                s[i] = 2
            else:
                # Neither 1 nor 2 is possible
                print("NO")
                return

    # If we successfully assigned all nodes, verify the solution.
    # The greedy logic ensures no local conflicts, but we must ensure
    # the assignment is globally consistent (the graph is bipartite).
    # The greedy assignment is consistent if and only if the graph is bipartite.
    # If the graph is not bipartite, the greedy algorithm will detect a conflict
    # when it tries to assign a value to a node that has neighbors with both 1 and 2.
    
    # Let's double check the constraints just to be absolutely sure.
    for u in range(1, n + 1):
        for v in adj[u]:
            if s[u] == s[v]:
                print("NO")
                return

    print("YES")
    print(*(s[1:]))

if __name__ == '__main__':
    solve()