import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    dependencies = []
    for i in range(m):
        u = int(data[3 + 2*i]) - 1  # Convert to 0-based indexing
        v = int(data[4 + 2*i]) - 1
        dependencies.append((u, v))
    
    # Try all permutations for small n
    if n <= 8:
        for perm in permutations(range(n)):
            total = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in dependencies:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1  # Convert back to 1-based
                print(' '.join(map(str, result)))
                return
        print("NO")
        return
    
    # For larger n, use heuristic: place node with most dependencies early
    # Count degree of each node
    degree = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in dependencies:
        degree[u] += 1
        degree[v] += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Heuristic: Start with node of highest degree at position 0
    # Then greedily place neighbors close
    order = [-1] * n
    placed = [False] * n
    pos = [0] * n
    
    # Find node with maximum degree
    max_deg = -1
    start_node = 0
    for i in range(n):
        if degree[i] > max_deg:
            max_deg = degree[i]
            start_node = i
    
    order[0] = start_node
    placed[start_node] = True
    pos[start_node] = 0
    
    # Greedily place remaining nodes
    for idx in range(1, n):
        best_node = -1
        best_pos = -1
        best_cost = float('inf')
        
        # Try all unplaced nodes
        for node in range(n):
            if placed[node]:
                continue
            # Try placing it at position idx
            new_pos = idx
            cost = 0
            for neighbor in adj[node]:
                if placed[neighbor]:
                    cost += abs(new_pos - pos[neighbor])
            if cost < best_cost:
                best_cost = cost
                best_node = node
                best_pos = new_pos
        
        if best_node != -1:
            order[idx] = best_node
            placed[best_node] = True
            pos[best_node] = best_pos
    
    # Calculate total cost of this arrangement
    total = 0
    for u, v in dependencies:
        total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[order[i]] = i + 1
        print(' '.join(map(str, result)))
        return
    
    # If greedy fails, try swapping adjacent elements to reduce cost
    improved = True
    while improved:
        improved = False
        current_total = 0
        for u, v in dependencies:
            current_total += abs(pos[u] - pos[v])
        if current_total > B:
            # Try all adjacent swaps
            for i in range(n - 1):
                # Swap order[i] and order[i+1]
                node1 = order[i]
                node2 = order[i+1]
                
                old_pos1 = pos[node1]
                old_pos2 = pos[node2]
                
                # Update positions
                pos[node1] = old_pos2
                pos[node2] = old_pos1
                
                new_total = 0
                for u, v in dependencies:
                    new_total += abs(pos[u] - pos[v])
                
                if new_total <= B:
                    print("YES")
                    result = [0] * n
                    for j in range(n):
                        result[order[j]] = j + 1
                    print(' '.join(map(str, result)))
                    return
                
                if new_total < current_total:
                    # Accept the swap
                    order[i], order[i+1] = order[i+1], order[i]
                    improved = True
                    break
                else:
                    # Revert the swap
                    pos[node1] = old_pos1
                    pos[node2] = old_pos2
    
    # Final check
    final_total = 0
    for u, v in dependencies:
        final_total += abs(pos[u] - pos[v])
    
    if final_total <= B:
        print("YES")
        result = [0] * n
        for i in range(n):
            result[order[i]] = i + 1
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()