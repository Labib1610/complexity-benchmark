import sys

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
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
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # Domains: bitmask of available colors {1, 2, 3}
    # 1<<1 | 1<<2 | 1<<3 = 2 + 4 + 8 = 14
    initial_domain = 14
    
    # Array to store the assignment
    assignment = [0] * n
    
    # Backtracking function
    # idx: current person index (0 to n-1)
    # domains: list of bitmasks for available colors of each person
    def backtrack(idx, domains):
        # Base case: all persons assigned
        if idx == n:
            return True
        
        # domains[idx] contains available colors for person idx
        # We try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for color in [1, 2, 3]:
            # Check if color is available for current person idx
            if (domains[idx] >> color) & 1:
                assignment[idx] = color
                
                # Prepare new domains for the next level
                # We copy the domains list to avoid modifying the parent's state
                new_domains = domains[:]
                
                # Check validity and update domains of neighbors > idx
                valid = True
                for neighbor in adj[idx]:
                    # Only need to check neighbors that are not yet assigned (neighbor > idx)
                    # Neighbors < idx are already assigned and their constraints were already
                    # checked when they were assigned (they removed 'color' from idx's domain).
                    if neighbor > idx:
                        new_domains[neighbor] &= ~(1 << color)
                        # If any neighbor has no available colors, this branch is invalid
                        if new_domains[neighbor] == 0:
                            valid = False
                            break
                
                if valid:
                    # Recurse to the next person
                    if backtrack(idx + 1, new_domains):
                        return True
        
        return False

    # Initial domains for all persons
    domains = [initial_domain] * n
    
    # Start backtracking from person 0
    if backtrack(0, domains):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()