import sys
from collections import defaultdict, deque

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        # No constraints, choose all 1s
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    graph = defaultdict(list)
    index = 2
    edges = []
    
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index + 1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # For each component, we can start with an arbitrary node and assign it a value.
    # Then propagate the constraints.
    # Since sum must be 3, if one node is x, the other must be 3 - x.
    # So this is a 2-coloring/BFS problem on each connected component.
    
    color = [-1] * n  # -1 means unvisited, 1 and 2 are the two "colors"
    
    # Check if bipartite for each component
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 1  # Start with color 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # Because 1 -> 2 and 2 -> 1
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # Now we have a valid coloring. We want the lexicographically smallest.
    # That means we prefer color 1 over 2 for earlier nodes.
    # But our BFS might not give that directly. 
    # However, since it's a valid 2-coloring, we can just take the one that starts with 1 for the first node,
    # unless there's a better way.
    # Actually, let's re-do the assignment to ensure lex smallest.
    
    # Let's do BFS again but always try to assign 1 to the earliest nodes if possible.
    # But since we already confirmed it's bipartite, any valid 2-coloring works.
    # The key insight is that for each connected component, there are only two valid assignments:
    # One where the first node (in order) is 1, and one where it's 2.
    # We want the one that gives lexicographically smaller sequence.
    
    # So, for each component, we can do BFS twice: once starting with 1, once with 2, 
    # and see which gives a lexicographically smaller result.
    # But that's overkill. Instead, let's just do a single BFS per component,
    # but make sure that among the two possible colorings, we pick the one that's lex smaller.
    
    # A simpler approach: 
    # Once we know it's bipartite, for each component, we can represent it as two sets L and R.
    # Then, we can assign all of L to 1 and R to 2, OR L to 2 and R to 1.
    # We choose based on which gives a smaller sequence.
    
    # Let's implement a proper solution:
    
    visited = [False] * n
    assignment = [0] * n  # 0 means unassigned
    
    for i in range(n):
        if not visited[i]:
            # Do BFS to get the component
            queue = deque()
            queue.append(i)
            visited[i] = True
            part1 = [i]  # Nodes at distance 0, 2, 4, ...
            part2 = []   # Nodes at distance 1, 3, 5, ...
            
            dist = [-1] * n
            dist[i] = 0
            
            while queue:
                node = queue.popleft()
                d = dist[node]
                
                for neighbor in graph[node]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = d + 1
                        queue.append(neighbor)
                        if (d + 1) % 2 == 0:
                            part1.append(neighbor)
                        else:
                            part2.append(neighbor)
            
            # Now decide whether to assign part1=1 or part1=2
            # We look at the first position where they differ
            assign1toPart1 = True
            
            # Find the minimum index in both parts
            min_part1 = min(part1) if part1 else float('inf')
            min_part2 = min(part2) if part2 else float('inf')
            
            if min_part1 < min_part2:
                # part1 has a node that comes earlier, so assign 1 to part1
                assign1toPart1 = True
            elif min_part2 < min_part1:
                # part2 has a node that comes earlier, so assign 1 to part2
                assign1toPart1 = False
            else:
                # Both have same minimal index node? This shouldn't happen in a connected component.
                # Actually, they are disjoint sets, so min indices are different.
                pass
            
            if assign1toPart1:
                for node in part1:
                    assignment[node] = 1
                for node in part2:
                    assignment[node] = 2
            else:
                for node in part1:
                    assignment[node] = 2
                for node in part2:
                    assignment[node] = 1
                    
    # Verify the solution
    for u, v in edges:
        if assignment[u] + assignment[v] != 3:
            print("NO")
            return
            
    print("YES")
    print(" ".join(str(x) for x in assignment))

solve()