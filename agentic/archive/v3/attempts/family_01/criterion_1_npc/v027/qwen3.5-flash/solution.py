import sys

# Increase recursion depth to handle N=40 safely
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
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

    # forbidden[v] stores a bitmask of colors used by neighbors < v
    # bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    forbidden = [0] * (n + 1)
    colors = [0] * (n + 1)

    def dfs(u):
        if u > n:
            return True

        # Try colors 1, 2, 3
        for c in range(1, 4):
            # Check if color c is allowed for u
            # It must not be used by any neighbor < u
            if not (forbidden[u] & (1 << (c - 1))):
                
                colors[u] = c
                
                changes = []
                conflict = False
                mask = 1 << (c - 1)
                
                # Forward checking: update forbidden for neighbors v > u
                for v in adj[u]:
                    if v > u:
                        # Only update if not already present
                        if not (forbidden[v] & mask):
                            forbidden[v] |= mask
                            changes.append(v)
                            # If all colors are forbidden, this path is invalid
                            if forbidden[v] == 7: # 111 binary
                                conflict = True
                                break
                    # If v < u, it's already colored, handled by forbidden[u] check above.
                
                if conflict:
                    # Backtrack changes
                    for v in changes:
                        forbidden[v] ^= mask
                    colors[u] = 0
                    continue

                # Recurse
                if dfs(u + 1):
                    return True
                
                # Backtrack changes
                for v in changes:
                    forbidden[v] ^= mask
                colors[u] = 0

        return False

    if dfs(1):
        print("YES")
        # Print colors separated by space
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()