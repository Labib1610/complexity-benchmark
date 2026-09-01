def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    # If no protocols, any assignment works, choose lexicographically smallest
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for i in range(m):
        u = int(data[2 + 2*i]) - 1  # Convert to 0-indexed
        v = int(data[3 + 2*i]) - 1
        edges.append((u, v))
    
    # Precompute energy for all possible level differences
    energy = {}
    for diff in range(-2, 3):
        energy[diff] = diff**4 - 5*diff**2 + 4
    
    # Check if a given assignment is stable
    def is_stable(colors):
        total = 0
        for u, v in edges:
            diff = colors[u] - colors[v]
            total += energy[diff]
        return total == 0
    
    # Generate all possible assignments in lexicographical order using backtracking
    def backtrack(pos, colors):
        if pos == n:
            if is_stable(colors):
                return colors[:]
            return None
        
        for c in [1, 2, 3]:
            colors[pos] = c
            # Check if current partial assignment can lead to a valid solution
            valid = True
            for u, v in edges:
                if u < pos and v < pos:  # Both nodes already assigned
                    diff = colors[u] - colors[v]
                    if energy[diff] < 0:
                        valid = False
                        break
            if not valid:
                continue
                
            result = backtrack(pos + 1, colors)
            if result is not None:
                return result
        return None
    
    # Start backtracking
    colors = [0] * n
    result = backtrack(0, colors)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

solve()