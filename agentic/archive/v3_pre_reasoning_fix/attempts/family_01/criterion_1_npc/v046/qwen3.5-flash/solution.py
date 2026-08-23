import sys

# Increase recursion depth just in case, though N=40 is small.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # forbidden[u] is a bitmask of colors forbidden for member u
    # bit 1 (value 1) -> shift 1 forbidden
    # bit 2 (value 2) -> shift 2 forbidden
    # bit 4 (value 4) -> shift 3 forbidden
    forbidden = [0] * (n + 1)
    ans = [0] * (n + 1)

    def dfs(u):
        if u > n:
            return True
        
        # Try shifts 1, 2, 3
        for c in range(1, 4):
            bit = 1 << (c - 1)
            
            # Check if shift c is allowed for u
            if (forbidden[u] & bit):
                continue
            
            # Assign shift c to u
            ans[u] = c
            
            # Forward checking: update forbidden colors for neighbors v > u
            changes = []
            possible = True
            
            for v in adj[u]:
                if v > u:
                    # If v doesn't have c forbidden yet, add it
                    if not (forbidden[v] & bit):
                        forbidden[v] |= bit
                        changes.append((v, bit))
                    
                    # If v has all 3 colors forbidden, this branch is invalid
                    if forbidden[v] == 7:
                        possible = False
                        break
            
            if possible:
                if dfs(u + 1):
                    return True
            
            # Backtrack: undo changes
            for v, bit in changes:
                forbidden[v] ^= bit
        
        # If no valid shift found for u
        ans[u] = 0
        return False

    if dfs(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()