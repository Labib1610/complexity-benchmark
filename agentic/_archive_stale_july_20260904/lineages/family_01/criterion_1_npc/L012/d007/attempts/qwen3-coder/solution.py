from itertools import product
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2

    # We need to try all 3^n combinations, but since n <= 40, this is infeasible.
    # However, we can use backtracking with pruning to find the minimal hash assignment.
    
    # Since we want the minimal hash, which is sum(c_i * 4^(n-i)), we should try assignments
    # in lexicographical order (since the coefficient 4^(n-i) decreases as i increases).
    # So we'll generate combinations in lex order and check constraints.
    
    # But even generating all combinations is too slow for n=40. Let's think differently.
    # Since there are only 3 colors, and dependencies form a graph where adjacent nodes
    # must have different colors (because det = c_u - c_v != 0), this is a graph coloring problem.
    # We need to check if the graph is 3-colorable.
    
    # If it's not 3-colorable, return NO.
    # If it is, we need to find the lexicographically smallest valid coloring.
    
    # Let's model this as a graph coloring problem.
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Check 3-colorability and find lex-min coloring
    color = [0] * n  # 0 means uncolored
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(pos):
        if pos == n:
            return True
        for c in [1, 2, 3]:
            if is_valid(pos, c):
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = 0
        return False
    
    if not backtrack(0):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()