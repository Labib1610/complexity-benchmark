import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # Result array to store assignments
    res = [0] * (n + 1)

    def is_consistent(node, color):
        """Check if assigning 'color' to 'node' violates any constraints with assigned neighbors."""
        for neighbor in adj[node]:
            if res[neighbor] == color:
                return False
        return True

    def can_color(node):
        """
        Backtracking check to see if the remaining nodes can be colored.
        Since n is small (up to 40), we use a simple backtracking with a bit of pruning.
        """
        if node > n:
            return True
        
        # Try colors in order 1, 2, 3 to maintain lexicographical order
        for color in (1, 2, 3):
            if is_consistent(node, color):
                res[node] = color
                if can_color(node + 1):
                    return True
                res[node] = 0
        return False

    # To find the lexicographically smallest sequence, we greedily try 1, then 2, then 3
    # for each node from 1 to n. For each choice, we check if a valid completion exists.
    
    final_assignment = [0] * (n + 1)
    
    def check_completion(current_node):
        """Checks if the current partial assignment can be completed to a valid 3-coloring."""
        # Use a local copy of res to avoid corrupting the main assignment during check
        temp_res = list(res)
        
        def backtrack(node):
            if node > n:
                return True
            # If node is already assigned (by the greedy outer loop), move to next
            if temp_res[node] != 0:
                return backtrack(node + 1)
            
            for color in (1, 2, 3):
                # Check consistency with neighbors
                consistent = True
                for neighbor in adj[node]:
                    if temp_res[neighbor] == color:
                        consistent = False
                        break
                if consistent:
                    temp_res[node] = color
                    if backtrack(node + 1):
                        return True
                    temp_res[node] = 0
            return False
        
        return backtrack(current_node + 1)

    # Greedy assignment for lexicographical smallest
    for i in range(1, n + 1):
        found = False
        for color in (1, 2, 3):
            if is_consistent(i, color):
                res[i] = color
                # Check if this choice allows for a valid completion of the rest of the graph
                if check_completion(i):
                    found = True
                    break
                res[i] = 0
        if not found:
            print("NO")
            return

    print("YES")
    print(*(res[1:]))

if __name__ == "__main__":
    # Increase recursion depth for backtracking
    sys.setrecursionlimit(2000)
    solve()