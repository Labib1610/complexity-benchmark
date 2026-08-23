import sys

# Increase recursion depth to handle N=40 safely.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list.
    # We only store neighbors v > u to optimize the inner loop during forward checking.
    # This is because we process vertices in order 1 to n.
    # When processing u, neighbors < u are already assigned, and neighbors > u are unassigned.
    # We need to update forbidden[v] for v > u.
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)
            
    # forbidden[u] is a bitmask of colors forbidden for u by already assigned neighbors.
    # Colors are 1, 2, 3, mapped to bits 0, 1, 2.
    # 1 -> 1 << 0
    # 2 -> 1 << 1
    # 3 -> 1 << 2
    forbidden = [0] * (n + 1)
    ans = [0] * (n + 1)
    
    def backtrack(u):
        # Base case: all tasks assigned
        if u > n:
            return True
        
        # Try assigning channels 1, 2, 3 in order (lexicographically smallest)
        for c in range(1, 4):
            # Check if channel c is valid for task u based on constraints from neighbors < u
            # forbidden[u] contains constraints from neighbors with index < u
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Forward checking: Check if assigning c to u makes any neighbor v > u impossible.
            # A neighbor v becomes impossible if all 3 colors are forbidden for it.
            # forbidden[v] currently holds constraints from neighbors < v (specifically neighbors < u and u's neighbors < u).
            # Actually, forbidden[v] holds constraints from assigned neighbors of v.
            # Since we are at step u, all neighbors of v with index < u are assigned.
            # If we assign c to u, and u is a neighbor of v, then c is added to forbidden[v].
            # If forbidden[v] | (1 << (c-1)) == 7, then v has 3 forbidden colors -> impossible.
            possible = True
            changes = []
            
            # Check potential conflicts with neighbors > u
            for v in adj[u]:
                # Check if v would have 3 forbidden colors
                if (forbidden[v] | (1 << (c - 1))) == 7:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # If valid, apply the constraint to neighbors > u
            mask = 1 << (c - 1)
            for v in adj[u]:
                forbidden[v] |= mask
                changes.append(v)
            
            # Assign channel c to u
            ans[u] = c
            
            # Recurse to next task
            if backtrack(u + 1):
                return True
            
            # Backtrack: undo changes
            ans[u] = 0
            for v in changes:
                forbidden[v] &= ~mask
        
        return False

    # Start backtracking from task 1
    if backtrack(1):
        print("YES")
        # Print the assignment sequence
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()