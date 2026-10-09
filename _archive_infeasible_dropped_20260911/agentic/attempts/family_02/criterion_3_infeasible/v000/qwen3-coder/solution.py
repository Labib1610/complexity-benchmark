import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build implication graph
    # Each variable x has two nodes: x (positive) and -x (negative)
    # We'll use node IDs: for variable i (1-based), 
    # node i represents (x_i = True), node -i represents (x_i = False)
    graph = defaultdict(list)
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # Clause (l1 OR l2) is equivalent to (~l1 -> l2) AND (~l2 -> l1)
        # In terms of implications:
        # If NOT l1, then l2 must be true => (-l1) implies (l2)
        # If NOT l2, then l1 must be true => (-l2) implies (l1)
        
        # ~l1 -> l2  translates to: if l1 is false, then l2 is true
        # Node -l1 connects to node l2
        graph[-l1].append(l2)
        
        # ~l2 -> l1 translates to: if l2 is false, then l1 is true  
        # Node -l2 connects to node l1
        graph[-l2].append(l1)
    
    # For each variable from 1 to n, check if it's forced to both values
    for var in range(1, n+1):
        # Check if var is forced to True and False simultaneously
        # This happens if there's a path from -var to +var AND from +var to -var
        
        def bfs(start, end):
            if start == end:
                return True
            visited = set()
            queue = deque([start])
            visited.add(start)
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v == end:
                        return True
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            return False
        
        # If there's a path from -var to +var, then var must be True
        # If there's a path from +var to -var, then var must be False
        # If both paths exist, var is trapped in contradiction
        if bfs(-var, var) and bfs(var, -var):
            print(var)
            return

if __name__ == "__main__":
    main()