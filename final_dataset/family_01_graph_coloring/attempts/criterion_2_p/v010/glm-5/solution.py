import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # We want the lexicographically smallest assignment.
    # A valid assignment is a valid 2-coloring of the graph.
    # Lexicographically smallest means we want s[i] = 1 as often as possible.
    # Since the components are independent, we can run BFS in order of nodes 1..n.
    # For each unvisited node u, we must set s[u] = 1 (lexicographically smallest choice).
    # Then we perform BFS to resolve constraints for the component.
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a new connected component
            # Lexicographically smallest choice: assign current node to 1
            color[i] = 1
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                
                # Sort neighbors to ensure deterministic processing order,
                # which helps maintain correctness logic though not strictly necessary for BFS validity
                # N.B. smaller neighbors processed first means their colors are set earlier.
                # This aligns with lexicographical goal: smaller index nodes get the smallest valid color.
                neighbors = sorted(adj[u])
                for v in neighbors:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    output = []
    if possible:
        output.append("YES")
        output.append(" ".join(map(str, color[1:])))
    else:
        output.append("NO")
    
    sys.stdout.write("\n".join(output))

if __name__ == '__main__':
    solve()