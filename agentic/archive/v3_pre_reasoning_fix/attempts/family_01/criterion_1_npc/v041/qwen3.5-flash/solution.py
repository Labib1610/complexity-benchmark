import sys

# Increase recursion depth to handle N=40 safely
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

    # adj_greater[u] will store neighbors of u that have index > u
    # This allows us to efficiently propagate constraints to future nodes
    adj_greater = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj_greater[u].append(v)
        else:
            adj_greater[v].append(u)

    # avail[u] is a bitmask representing available colors for node u
    # Colors are 1, 2, 3. We use bits 0, 1, 2.
    # Initially all colors are available (111 binary = 7)
    avail = [7] * (n + 1)
    color = [0] * (n + 1)
    
    def dfs(u):
        # If we have successfully assigned shifts to all n staff members
        if u > n:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, color[1:n+1])) + "\n")
            sys.exit(0)
        
        # If no colors are available for the current staff member, this path is invalid
        if avail[u] == 0:
            return False

        # Try assigning shifts 1, 2, 3 in order to ensure lexicographically smallest result
        for c in (1, 2, 3):
            # Check if color c is available for u
            if (avail[u] >> (c - 1)) & 1:
                mask = 1 << (c - 1)
                modified = []
                possible = True
                
                # Forward checking: remove color c from available colors of neighbors v > u
                for v in adj_greater[u]:
                    if (avail[v] & mask):
                        avail[v] &= ~mask
                        modified.append(v)
                        # If a neighbor has no available colors left, this path is invalid
                        if avail[v] == 0:
                            possible = False
                            break
                
                if possible:
                    color[u] = c
                    if dfs(u + 1):
                        return True
                    color[u] = 0
                
                # Backtrack: restore available colors for modified neighbors
                for v in modified:
                    avail[v] |= mask
        
        return False

    # Start DFS from staff member 1
    dfs(1)
    
    # If DFS returns without finding a solution, output NO
    print("NO")

if __name__ == '__main__':
    solve()