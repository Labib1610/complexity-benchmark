import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    # Using sys.stdin.read().split() handles whitespace and newlines automatically
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list for the graph
    # Using 1-based indexing for sensors
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Array to store the phase setting for each sensor
    # 0: unassigned, 1: phase 1, 2: phase 2
    phase = [0] * (n + 1)
    
    # Iterate through all sensors to handle disconnected components
    # We process sensors in increasing order of their index.
    # This greedy approach ensures lexicographically smallest sequence because
    # for any connected component, the node with the smallest index is processed first,
    # and we assign it phase 1 (the smallest possible value).
    for i in range(1, n + 1):
        if phase[i] == 0:
            # Start BFS from the smallest index node in the component
            phase[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_phase = phase[u]
                next_phase = 3 - current_phase  # Switch between 1 and 2
                
                for v in adj[u]:
                    if phase[v] == 0:
                        phase[v] = next_phase
                        queue.append(v)
                    elif phase[v] == current_phase:
                        # Conflict detected: adjacent sensors have the same phase
                        # This implies the graph is not bipartite
                        print("NO")
                        return
    
    # If no conflicts found, output YES and the configuration
    print("YES")
    # Join with space for output format
    sys.stdout.write(' '.join(map(str, phase[1:])) + '\n')

if __name__ == '__main__':
    solve()