import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # We need to assign values 1 or 2 to each node such that for every edge (u,v):
    # (u % v) + (v % u) = 1
    # Let's analyze what this means:
    # If both are 1: (1%1)+(1%1) = 0+0 = 0 ≠1
    # If one is 1 and other is 2: (1%2)+(2%1) = 1+0 =1 ✓
    # If both are 2: (2%2)+(2%2) = 0+0 =0 ≠1
    # So adjacent nodes must have different values.
    # This is a bipartite graph check.
    
    color = [0] * (n + 1)  # 0=unvisited, 1=color1, 2=color2
    
    # Check if the graph is bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            color[start] = 1
            queue.append(start)
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1↔2
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest assignment
    # We want to minimize the sequence, so we prefer assigning 1 to lower-numbered nodes when possible
    # But we must respect the bipartite coloring.
    # In a connected component, once we choose a color for one node, the rest are determined.
    # To get lex smallest, in each component, we choose whether to map color 1 to value 1 or 2,
    # based on which gives a smaller lex order.
    
    # Let's re-color to get lex smallest result
    result = [0] * (n + 1)
    
    visited_component = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited_component[i]:
            # Find the entire component
            component_nodes = []
            queue = deque()
            queue.append(i)
            visited_component[i] = True
            component_nodes.append(i)
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited_component[neighbor]:
                        visited_component[neighbor] = True
                        component_nodes.append(neighbor)
                        queue.append(neighbor)
            
            # Extract subgraph induced by component_nodes
            # Decide whether to map color 1 to 1 or 2 to get lex smallest
            # Try both options and see which is better
            
            # Get the colors in the component
            c1_nodes = [x for x in component_nodes if color[x] == 1]
            c2_nodes = [x for x in component_nodes if color[x] == 2]
            
            # Option 1: color 1 -> 1, color 2 -> 2
            option1 = {}
            for x in c1_nodes:
                option1[x] = 1
            for x in c2_nodes:
                option1[x] = 2
                
            # Option 2: color 1 -> 2, color 2 -> 1
            option2 = {}
            for x in c1_nodes:
                option2[x] = 2
            for x in c2_nodes:
                option2[x] = 1
                
            # Compare the sequences
            seq1 = [option1[x] for x in sorted(component_nodes)]
            seq2 = [option2[x] for x in sorted(component_nodes)]
            
            chosen_option = option1 if seq1 <= seq2 else option2
            
            for x in component_nodes:
                result[x] = chosen_option[x]
                
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()