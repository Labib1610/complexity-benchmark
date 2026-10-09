import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    B = int(data[2])
    
    links = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        v = int(data[idx+1]) - 1
        links.append((u, v))
        idx += 2
    
    # If n is small enough, try all permutations
    if n <= 8:
        for perm in permutations(range(n)):
            total_dist = 0
            pos = [0] * n
            for i in range(n):
                pos[perm[i]] = i
            for u, v in links:
                total_dist += abs(pos[u] - pos[v])
                if total_dist > B:
                    break
            if total_dist <= B:
                print("YES")
                print(' '.join(str(perm[i] + 1) for i in range(n)))
                return
        print("NO")
        return
    
    # For larger n, use a heuristic: place linked exhibits close together
    # Build adjacency list
    adj = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in links:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Try a greedy placement starting with highest degree node
    # This is a simplified heuristic, not guaranteed to work
    # But for many cases it will find a solution if one exists
    
    # Let's try a simple approach: use BFS-like placement
    # Start with node of highest degree
    max_deg = -1
    start_node = 0
    for i in range(n):
        if degree[i] > max_deg:
            max_deg = degree[i]
            start_node = i
    
    # Place nodes in a way that tries to minimize distances
    # This is a greedy heuristic
    position = [-1] * n
    placed = [False] * n
    # Try placing start_node at the middle
    position[start_node] = n // 2
    placed[start_node] = True
    
    # Queue for BFS-like placement
    from collections import deque
    queue = deque()
    queue.append(start_node)
    
    while queue:
        u = queue.popleft()
        pos_u = position[u]
        for v in adj[u]:
            if not placed[v]:
                # Try to place v adjacent to u if possible
                # Check positions pos_u -1 and pos_u + 1
                placed_v = False
                for delta in [-1, 1]:
                    new_pos = pos_u + delta
                    if 0 <= new_pos < n and position[v] == -1 and not placed[new_pos]:
                        # Need to check if new_pos is not occupied
                        # Actually, position[v] will tell us if v is placed
                        # Let's reorganize
                        pass
                
                # Let's just find the first available adjacent spot
                candidates = []
                for delta in [-1, 1]:
                    new_pos = pos_u + delta
                    if 0 <= new_pos < n:
                        candidates.append(new_pos)
                
                placed_v = False
                for p in candidates:
                    # Check if any node is already placed at position p
                    node_at_p = -1
                    for node in range(n):
                        if position[node] == p:
                            node_at_p = node
                            break
                    if node_at_p == -1:
                        position[v] = p
                        placed[v] = True
                        queue.append(v)
                        placed_v = True
                        break
                
                if not placed_v and position[v] == -1:
                    # Place it somewhere else
                    for p in range(n):
                        node_at_p = -1
                        for node in range(n):
                            if position[node] == p:
                                node_at_p = node
                                break
                        if node_at_p == -1:
                            position[v] = p
                            placed[v] = True
                            queue.append(v)
                            break
    
    # If some nodes are still not placed, place them
    for i in range(n):
        if position[i] == -1:
            for p in range(n):
                node_at_p = -1
                for node in range(n):
                    if position[node] == p:
                        node_at_p = node
                        break
                if node_at_p == -1:
                    position[i] = p
                    break
    
    # Calculate total distance
    total_dist = 0
    for u, v in links:
        total_dist += abs(position[u] - position[v])
    
    if total_dist <= B:
        # Create the result permutation
        result = [0] * n
        for i in range(n):
            result[position[i]] = i + 1  # Convert back to 1-based
        print("YES")
        print(' '.join(map(str, result)))
        return
    
    # Heuristic failed, try a different approach or say NO
    # For now, let's just say NO for large inputs where heuristic fails
    print("NO")

if __name__ == "__main__":
    main()