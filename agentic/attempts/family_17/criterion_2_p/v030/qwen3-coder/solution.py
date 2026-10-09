from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Create adjacency list for bipartite graph
    # Left side: 1 to q, Right side: q+1 to 2q
    graph = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # Try to find maximum matching using BFS (Hopcroft-Karp like approach)
    # But since we need a perfect matching, we can use a simpler approach
    # Use greedy matching first, then augmenting paths if needed
    
    match_right = {}  # match_right[b] = a means b is matched to a
    match_left = {}   # match_left[a] = b means a is matched to b
    
    # Build initial matching with greedy approach
    for a in range(1, q + 1):
        for b in graph[a]:
            if b not in match_right:
                match_left[a] = b
                match_right[b] = a
                break
    
    # Function to find augmenting path
    def find_augmenting_path():
        # BFS to find shortest augmenting path
        visited_left = set()
        visited_right = set()
        queue = deque()
        
        # Add all unmatched left vertices to queue
        for a in range(1, q + 1):
            if a not in match_left:
                queue.append(('L', a))
                visited_left.add(a)
        
        parent = {}  # To reconstruct path
        
        while queue:
            side, node = queue.popleft()
            
            if side == 'L':
                a = node
                # Check all neighbors
                for b in graph[a]:
                    if b in visited_right:
                        continue
                    visited_right.add(b)
                    parent[('R', b)] = ('L', a)
                    
                    if b not in match_right:
                        # Found augmenting path
                        # Reconstruct path and update matching
                        current_side, current_node = 'R', b
                        path = []
                        while True:
                            path.append((current_side, current_node))
                            if (current_side, current_node) in parent:
                                current_side, current_node = parent[(current_side, current_node)]
                            else:
                                break
                        
                        path.reverse()
                        
                        # Update matching along the path
                        for i in range(0, len(path)-1, 2):
                            a_node = path[i][1]
                            b_node = path[i+1][1]
                            # Remove old matching if exists
                            if b_node in match_right:
                                old_a = match_right[b_node]
                                del match_left[old_a]
                            # Add new matching
                            match_left[a_node] = b_node
                            match_right[b_node] = a_node
                        return True
                    
                    # Continue BFS from matched partner
                    matched_a = match_right[b]
                    if matched_a not in visited_left:
                        visited_left.add(matched_a)
                        parent[('L', matched_a)] = ('R', b)
                        queue.append(('L', matched_a))
        
        return False
    
    # Keep finding augmenting paths until no more exist
    while find_augmenting_path():
        pass
    
    # Check if we have a perfect matching
    if len(match_left) == q:
        print("YES")
        for a in range(1, q + 1):
            print(a, match_left[a])
    else:
        print("NO")

solve()