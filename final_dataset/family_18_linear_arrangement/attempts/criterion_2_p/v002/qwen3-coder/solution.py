import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    n, m, B = map(int, sys.stdin.readline().split())
    
    if n == 1:
        if 0 <= B:
            print("YES")
            print(1)
        else:
            print("NO")
        return
    
    # Build adjacency list and find root
    children = defaultdict(list)
    parent = [-1] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        children[u].append(v)
        parent[v] = u
    
    # Find root (the one with no parent)
    root = None
    for i in range(1, n + 1):
        if parent[i] == -1:
            root = i
            break
    
    # Compute subtree sizes
    size = [0] * (n + 1)
    
    def compute_size(node):
        sz = 1
        for child in children[node]:
            sz += compute_size(child)
        size[node] = sz
        return sz
    
    compute_size(root)
    
    # Assign positions using DFS in-order traversal
    position = [0] * (n + 1)
    current_time = 1
    
    def assign_positions(node):
        nonlocal current_time
        # Assign to leftmost available slot
        if not children[node]:
            position[node] = current_time
            current_time += 1
            return
        
        # For better ordering, sort children by their subtree sizes (largest first)
        # This helps minimize the total cost
        sorted_children = sorted(children[node], key=lambda x: -size[x])
        
        # Process first child
        assign_positions(sorted_children[0])
        
        # Assign current node
        position[node] = current_time
        current_time += 1
        
        # Process remaining children
        for i in range(1, len(sorted_children)):
            assign_positions(sorted_children[i])
    
    assign_positions(root)
    
    # Calculate total cost
    total_cost = 0
    for node in range(1, n + 1):
        for child in children[node]:
            total_cost += abs(position[node] - position[child])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, position[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()