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

    # To get lexicographically smallest sequence, we want to assign shift 1
    # to the smallest-indexed worker whenever possible.
    # We iterate workers from 1 to n. If a worker is unassigned, we try to
    # assign them shift 1. This triggers a DFS/BFS to assign their component.
    # The DFS prioritizes assigning shift 1 to the smallest-indexed neighbor
    # to propagate the lexicographically smallest choices.
    
    color = [0] * (n + 1)
    
    # Stack for DFS: stores (node, parent)
    # We use iterative DFS to avoid recursion depth issues.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a DFS from i, trying to color it with 1
            stack = [(i, 1)]
            
            while stack:
                u, c = stack.pop()
                
                if color[u] != 0:
                    # Already visited, check consistency
                    if color[u] != c:
                        print("NO")
                        return
                    continue
                
                color[u] = c
                
                # To ensure lexicographically smallest sequence, we should
                # try to assign shift 1 to smaller indexed neighbors first.
                # Since we use a stack, we push larger indexed neighbors first
                # so that smaller ones are processed first.
                
                # Sort neighbors in descending order to push onto stack
                # so that smallest is popped first.
                neighbors = sorted(adj[u], reverse=True)
                
                for v in neighbors:
                    if color[v] == 0:
                        stack.append((v, 3 - c))
                    elif color[v] == c:
                        print("NO")
                        return

    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()