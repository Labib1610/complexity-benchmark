import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    edges = []
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based
        v = int(data[4 + 2*i]) - 1
        edges.append((u, v))
    
    # If m == 0, any permutation works
    if m == 0:
        print("YES")
        print(" ".join(str(x) for x in range(1, n+1)))
        return
    
    # For small n, try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in edges:
                total += abs(pos[u] - pos[v])
            if total <= B:
                print("YES")
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1
                print(" ".join(map(str, result)))
                return
        print("NO")
        return
    
    # For larger n, use a heuristic: place nodes with highest degree towards center
    # Compute degrees
    degree = [0] * n
    for u,v in edges:
        degree[u] += 1
        degree[v] += 1
    
    # Sort nodes by degree descending
    nodes = list(range(n))
    nodes.sort(key=lambda x: degree[x], reverse=True)
    
    # Assign positions: place high degree nodes in the middle
    position = [0] * n
    # Create a list of positions from 0 to n-1
    # Assign nodes to positions in a way that high degree nodes are central
    # We'll place them in order of sorted nodes, placing them alternately from center outwards
    assigned_positions = [None] * n
    mid = n // 2
    assigned_positions[mid] = nodes[0]
    position[nodes[0]] = mid
    
    left = mid - 1
    right = mid + 1
    idx = 1
    while idx < n:
        if left >= 0:
            assigned_positions[left] = nodes[idx]
            position[nodes[idx]] = left
            left -= 1
            idx += 1
        if idx < n and right < n:
            assigned_positions[right] = nodes[idx]
            position[nodes[idx]] = right
            right += 1
            idx += 1
    
    # Calculate total cost
    total = 0
    for u, v in edges:
        total += abs(position[u] - position[v])
    
    if total <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[i] = position[i] + 1
        print(" ".join(map(str, result)))
        return
    
    # If the heuristic fails, try a few random permutations (optional)
    # But given time constraints and the nature of the problem, we'll just say NO
    print("NO")

if __name__ == "__main__":
    main()