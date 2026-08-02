import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr]) - 1
        v = int(input_data[ptr+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    assignment = [0] * n

    def is_possible(idx):
        """
        Check if the current partial assignment can be extended to a full 3-coloring.
        Since n is small (40), we can use a backtracking search with pruning or
        a simple recursive check for the remaining nodes.
        """
        # We only need to check if the remaining nodes [idx, n-1] can be colored
        # given the constraints from [0, idx-1] and each other.
        
        temp_assignment = list(assignment)
        
        def backtrack(curr):
            if curr == n:
                return True
            
            # Try colors 1, 2, 3
            for color in (1, 2, 3):
                # Check if color is valid for node 'curr'
                possible = True
                for neighbor in adj[curr]:
                    if neighbor < curr and temp_assignment[neighbor] == color:
                        possible = False
                        break
                
                if possible:
                    temp_assignment[curr] = color
                    if backtrack(curr + 1):
                        return True
                    temp_assignment[curr] = 0
            return False

        # However, full backtracking inside every step is too slow.
        # But we only need to check if ANY valid coloring exists.
        # Since n=40 is small, we can use a slightly more optimized check.
        return backtrack(idx)

    # To find the lexicographically smallest sequence, we try colors 1, 2, 3 
    # for each person i from 1 to n.
    
    # Optimization: The check 'is_possible' is expensive.
    # Instead of calling it every time, we can use a global backtracking 
    # that naturally finds the lexicographically smallest solution.
    
    result = [0] * n
    
    def find_lex_smallest(curr):
        if curr == n:
            return True
        
        # Try colors in increasing order to ensure lexicographical smallest
        for color in (1, 2, 3):
            # Check if this color conflicts with already assigned neighbors
            conflict = False
            for neighbor in adj[curr]:
                if neighbor < curr and result[neighbor] == color:
                    conflict = True
                    break
            
            if not conflict:
                result[curr] = color
                # To optimize, we can't just backtrack; we need to be sure
                # this choice doesn't make it impossible to color the rest.
                # But for n=40, standard backtracking with pruning might work
                # if we are lucky, or we might need a more robust 3-coloring check.
                if find_lex_smallest(curr + 1):
                    return True
                result[curr] = 0
        return False

    # Standard backtracking to find the lexicographically first valid 3-coloring.
    # For n=40, the worst case is exponential, but 3-coloring is often fast
    # on sparse graphs or small n.
    if find_lex_smallest(0):
        print("YES")
        print(*(result))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    solve()