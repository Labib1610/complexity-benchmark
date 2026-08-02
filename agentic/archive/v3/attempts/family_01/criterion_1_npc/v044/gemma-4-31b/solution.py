import sys

def solve():
    # Read n and m
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
    except ValueError:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # The problem asks for the lexicographically smallest sequence (s1, s2, ..., sn).
    # We can determine each s_i greedily from 1 to n.
    # For each i, we try s_i = 1, then 2, then 3.
    # For each choice, we must check if a valid 3-coloring exists for the remaining technicians.
    
    current_assignment = [0] * n

    def is_3_colorable(assigned_count):
        # Check if the current partial assignment can be extended to a full 3-coloring.
        # Since N is small (up to 40), we can use backtracking with pruning.
        
        # To speed up, we only need to check if the remaining nodes can be colored.
        # However, the constraints are tight, so a simple backtracking might be slow.
        # We use a basic backtracking with a simple heuristic (MRV - Minimum Remaining Values).
        
        remaining = []
        for i in range(assigned_count, n):
            remaining.append(i)
            
        # We need to check if there exists any valid assignment for nodes [assigned_count...n-1]
        # given the constraints from [0...assigned_count-1] and each other.
        
        temp_assignment = list(current_assignment)
        
        def backtrack(idx):
            if idx == n:
                return True
            
            # Heuristic: pick the node with the fewest available colors (MRV)
            # For simplicity in Python, we just go sequentially or use a simple loop.
            # Given N=40, sequential might be too slow, but we only call this 
            # at most 3*N times.
            
            u = idx
            # Try colors 1, 2, 3
            for color in (1, 2, 3):
                can_use = True
                for v in adj[u]:
                    if v < n and temp_assignment[v] == color:
                        can_use = False
                        break
                if can_use:
                    temp_assignment[u] = color
                    if backtrack(idx + 1):
                        return True
                    temp_assignment[u] = 0
            return False

        # Since we are checking 3-colorability (NP-complete), 
        # and N=40 is small but not tiny, we need an efficient check.
        # A simple backtracking with a bit of pruning:
        
        def solve_coloring(node_idx):
            if node_idx == n:
                return True
            
            # Try colors 1, 2, 3
            for c in (1, 2, 3):
                possible = True
                for neighbor in adj[node_idx]:
                    if neighbor < node_idx and temp_assignment[neighbor] == c:
                        possible = False
                        break
                    # Note: neighbors > node_idx are not assigned yet
                if possible:
                    temp_assignment[node_idx] = c
                    if solve_coloring(node_idx + 1):
                        return True
                    temp_assignment[node_idx] = 0
            return False

        # However, the partial assignment is already set for 0...assigned_count-1.
        # We only need to fill assigned_count...n-1.
        return solve_coloring(assigned_count)

    # To make the 3-coloring check faster, we can use a more optimized version.
    # Because we call this function frequently, efficiency is key.
    
    def fast_check(assigned_count):
        # Using a basic backtracking with a bit of pruning
        state = list(current_assignment)
        
        def backtrack(u):
            if u == n:
                return True
            
            # Find available colors for u
            used = 0
            for v in adj[u]:
                if v < u: # Only check already assigned neighbors
                    if state[v] != 0:
                        used |= (1 << state[v])
            
            for c in (1, 2, 3):
                if not (used & (1 << c)):
                    state[u] = c
                    if backtrack(u + 1):
                        return True
                    state[u] = 0
            return False
        
        return backtrack(assigned_count)

    # Lexicographical greedy approach
    for i in range(n):
        found = False
        for color in (1, 2, 3):
            # Check if 'color' is compatible with already assigned neighbors
            compatible = True
            for v in adj[i]:
                if v < i and current_assignment[v] == color:
                    compatible = False
                    break
            
            if compatible:
                current_assignment[i] = color
                if fast_check(i + 1):
                    found = True
                    break
                current_assignment[i] = 0
        
        if not found:
            print("NO")
            return

    print("YES")
    print(*(current_assignment))

if __name__ == "__main__":
    solve()