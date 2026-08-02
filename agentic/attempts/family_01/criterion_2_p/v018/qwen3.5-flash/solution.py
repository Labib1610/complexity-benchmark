import sys

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    # Nodes are 1-indexed, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Color array: 0 = unvisited, 1 = block 1, 2 = block 2
    color = [0] * (n + 1)
    
    # Iterate through all individuals to handle disconnected components.
    # We process individuals in increasing order of their labels (1 to n).
    # For each unassigned individual, we start a traversal (BFS) to assign blocks.
    # To achieve the lexicographically smallest sequence, we always assign the first 
    # encountered node in a component (which is the smallest index in that component)
    # to block 1. The rest of the component is then determined by the bipartite constraint.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Assign block 1 to the starting node
            color[i] = 1
            
            # Use a list as a queue for BFS
            queue = [i]
            head = 0
            
            while head < len(queue):
                u = queue[head]
                head += 1
                
                current_block = color[u]
                next_block = 3 - current_block  # Switch between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_block
                        queue.append(v)
                    elif color[v] != next_block:
                        # Incompatible pair assigned to the same block
                        print("NO")
                        return

    # If valid assignment exists
    print("YES")
    # Output the assignments for individuals 1 to n
    # Using sys.stdout.write for faster I/O
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()