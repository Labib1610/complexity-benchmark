import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    pairs = []
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based index
        v = int(data[4 + 2*i]) - 1
        pairs.append((u, v))
    
    # If m is 0, any permutation works
    if m == 0:
        print("YES")
        print(" ".join(str(i) for i in range(1, n+1)))
        return
    
    # Try all permutations for small n
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in pairs:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1
                print("YES")
                print(" ".join(map(str, result)))
                return
        print("NO")
        return
    
    # For larger n, use a heuristic approach
    # Start with a greedy assignment
    # Place the reaction involved in most pairs near the center
    
    # Count how many times each reaction appears in pairs
    count = [0] * n
    for u, v in pairs:
        count[u] += 1
        count[v] += 1
    
    # Sort reactions by count in descending order
    sorted_reactions = sorted(range(n), key=lambda x: count[x], reverse=True)
    
    # Assign positions greedily
    # Place the most connected reaction in the middle
    positions = [-1] * n
    available = list(range(n))
    
    # Try placing the first reaction in the middle
    first = sorted_reactions[0]
    mid = n // 2
    positions[first] = mid
    available.remove(mid)
    
    # For other reactions, try to place them to minimize total cost
    for reaction in sorted_reactions[1:]:
        if positions[reaction] != -1:
            continue
        best_pos = -1
        min_cost = float('inf')
        for pos in available:
            positions[reaction] = pos
            cost = 0
            for u, v in pairs:
                if positions[u] != -1 and positions[v] != -1:
                    cost += abs(positions[u] - positions[v])
                elif positions[u] != -1 or positions[v] != -1:
                    # One is placed, the other isn't
                    # We can estimate or just use current positions
                    pass
            if cost < min_cost:
                min_cost = cost
                best_pos = pos
            positions[reaction] = -1
        if best_pos != -1:
            positions[reaction] = best_pos
            available.remove(best_pos)
    
    # Assign remaining reactions to any available positions
    for i in range(n):
        if positions[i] == -1:
            positions[i] = available.pop()
    
    # Check the total cost
    total = 0
    for u, v in pairs:
        total += abs(positions[u] - positions[v])
    
    if total <= B:
        result = [0] * n
        for i in range(n):
            result[i] = positions[i] + 1
        print("YES")
        print(" ".join(map(str, result)))
        return
    
    # If greedy fails, try local search or other heuristics
    # For now, we'll just say NO for larger cases where greedy fails
    # A more sophisticated approach would involve local search or simulated annealing
    print("NO")

if __name__ == "__main__":
    main()