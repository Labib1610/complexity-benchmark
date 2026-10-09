import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    # Check if the graph is 3-colorable
    # Since n <= 40, we can use meet-in-the-middle
    # Split vertices into two halves
    n1 = n // 2
    n2 = n - n1
    vertices1 = list(range(n1))
    vertices2 = list(range(n1, n))

    # Precompute internal conflicts for each half
    # For each subset mask, check if it's an independent set
    # We'll use this to check valid colorings

    # For the first half
    # valid_colorings1 will store all valid 3-colorings of the first half
    # Each coloring is represented as a tuple of colors (length n1)
    # We can iterate through all 3^n1 possibilities and check validity
    
    # To speed up, we can precompute for each vertex its neighbors in the same half
    adj1 = [set() for _ in range(n1)]
    for i in range(n1):
        for j in range(n1):
            if j in adj[i]:
                adj1[i].add(j)

    adj2 = [set() for _ in range(n2)]
    for i in range(n2):
        for j in range(n2):
            if (n1 + j) in adj[n1 + i]:
                adj2[i].add(j)

    # Precompute cross conflicts
    # cross_conflicts[i][j] = True if vertex i in first half conflicts with vertex j in second half
    cross_conflicts = [[False] * n2 for _ in range(n1)]
    for i in range(n1):
        for j in range(n2):
            if (n1 + j) in adj[i]:
                cross_conflicts[i][j] = True

    # Generate all valid colorings for the first half
    # Using iterative approach with pruning
    valid1 = []
    colors1 = [0] * n1
    
    def dfs1(idx):
        if idx == n1:
            valid1.append(colors1[:])
            return
        for c in range(3):
            # Check if color c is valid for vertex idx
            ok = True
            for neighbor in adj1[idx]:
                if neighbor < idx and colors1[neighbor] == c:
                    ok = False
                    break
            if ok:
                colors1[idx] = c
                dfs1(idx + 1)
    
    dfs1(0)

    # Generate all valid colorings for the second half
    valid2 = []
    colors2 = [0] * n2
    
    def dfs2(idx):
        if idx == n2:
            valid2.append(colors2[:])
            return
        for c in range(3):
            ok = True
            for neighbor in adj2[idx]:
                if neighbor < idx and colors2[neighbor] == c:
                    ok = False
                    break
            if ok:
                colors2[idx] = c
                dfs2(idx + 1)
    
    dfs2(0)

    # Now we need to find a pair of colorings (c1, c2) such that
    # for all cross conflicts (i, j), c1[i] != c2[j]
    # We can use meet-in-the-middle:
    # For each valid coloring of the second half, compute a "signature"
    # that represents the forbidden colors for each vertex in the first half
    # Then for each valid coloring of the first half, check if it matches

    # For efficiency, we'll represent the constraints from the second half
    # For each vertex i in the first half, the forbidden colors are those
    # assigned to its conflicting neighbors in the second half
    
    # We'll iterate through valid2 and build a hash map
    # Key: for each vertex i in first half, the set of forbidden colors
    # But this is complex, so we'll use a simpler approach:
    # For each valid coloring c2, compute a bitmask for each vertex i in first half
    # indicating which colors are forbidden (due to conflicts with c2)
    # Then for each valid coloring c1, check if c1[i] is not forbidden for all i

    # To speed up, we'll precompute for each valid2 a forbidden mask for each vertex in first half
    # forbidden_mask[i] is a 3-bit mask where bit c is set if color c is forbidden for vertex i
    
    # Build a hash map: for each forbidden_mask configuration, store the corresponding c2
    # But forbidden_mask is a tuple of n1 integers, which can be large
    # Instead, we'll iterate through valid1 and valid2 and check compatibility
    
    # Since n <= 40, n1 <= 20, n2 <= 20
    # The number of valid colorings can be up to 3^20 in worst case, but usually much smaller
    # due to conflicts
    
    # For this problem, we'll use a direct check with some optimization
    # Precompute for each valid2, the forbidden colors for each vertex in first half
    
    # To optimize, we'll use a hash map where key is the forbidden mask for each vertex
    # But since n1 can be up to 20, we'll use a different approach:
    # For each valid2, compute a hash of the forbidden configuration
    # Then for each valid1, compute the required forbidden configuration and check
    
    # Actually, let's just iterate and check directly
    # Given the constraints, this should be fast enough
    
    for c1 in valid1:
        for c2 in valid2:
            ok = True
            for i in range(n1):
                if not ok:
                    break
                for j in range(n2):
                    if cross_conflicts[i][j] and c1[i] == c2[j]:
                        ok = False
                        break
            if ok:
                # Found a valid coloring
                result = [0] * n
                for i in range(n1):
                    result[i] = c1[i] + 1  # Convert to 1-based
                for j in range(n2):
                    result[n1 + j] = c2[j] + 1
                print("YES")
                print(" ".join(map(str, result)))
                return

    print("NO")

if __name__ == "__main__":
    solve()