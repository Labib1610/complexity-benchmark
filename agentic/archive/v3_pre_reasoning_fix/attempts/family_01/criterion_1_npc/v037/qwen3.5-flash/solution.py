import sys

# Increase recursion depth to handle deep recursion in backtracking
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
        
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    ans = [0] * (n + 1)
    
    # Helper function to check if the remaining graph (vertices start_idx to n)
    # can be colored given the fixed colors in current_ans[1...start_idx-1].
    def check_feasible(start_idx, current_ans):
        if start_idx > n:
            return True
        
        # available[v] stores a bitmask of allowed colors for vertex v
        # 1 -> color 1, 2 -> color 2, 4 -> color 4
        # Initially all colors are available (7 = 111 binary)
        available = [7] * (n + 1)
        
        # Apply constraints from already colored vertices
        for i in range(1, start_idx):
            c = current_ans[i]
            if c != 0:
                forbidden = 1 << (c - 1)
                for v in adj[i]:
                    if v >= start_idx:
                        available[v] &= ~forbidden
        
        # Check if any vertex has no available colors
        for v in range(start_idx, n + 1):
            if available[v] == 0:
                return False
        
        # List of uncolored vertices
        uncolored = list(range(start_idx, n + 1))
        # Boolean array to quickly check if a vertex is uncolored
        is_uncolored = [False] * (n + 1)
        for v in uncolored:
            is_uncolored[v] = True
            
        def backtrack():
            if not uncolored:
                return True
            
            # Unit propagation: if any vertex has exactly 1 color available, it's forced
            for v in uncolored:
                # Count set bits in available[v] manually for efficiency
                cnt = 0
                if available[v] & 1: cnt += 1
                if available[v] & 2: cnt += 1
                if available[v] & 4: cnt += 1
                
                if cnt == 1:
                    # Forced move
                    color_bit = available[v]
                    
                    # Remove v from uncolored
                    uncolored.remove(v)
                    is_uncolored[v] = False
                    
                    # Update neighbors
                    for v2 in adj[v]:
                        if is_uncolored[v2]:
                            available[v2] &= ~color_bit
                    
                    res = backtrack()
                    
                    if res: return True
                    
                    # Backtrack: restore state
                    is_uncolored[v] = True
                    uncolored.append(v)
                    for v2 in adj[v]:
                        if is_uncolored[v2]:
                            available[v2] |= color_bit
                    
                    # If forced move didn't lead to solution, then no solution exists from this state
                    return False
            
            # MRV (Minimum Remaining Values) heuristic
            best_v = -1
            best_count = 4
            for v in uncolored:
                cnt = 0
                if available[v] & 1: cnt += 1
                if available[v] & 2: cnt += 1
                if available[v] & 4: cnt += 1
                
                if cnt < best_count:
                    best_count = cnt
                    best_v = v
                    if cnt == 1: break
            
            if best_count == 0:
                return False
            
            # Try assigning colors to best_v
            # Order doesn't matter for feasibility check
            for color_bit in [1, 2, 4]:
                if available[best_v] & color_bit:
                    # Assign color
                    uncolored.remove(best_v)
                    is_uncolored[best_v] = False
                    
                    for v2 in adj[best_v]:
                        if is_uncolored[v2]:
                            available[v2] &= ~color_bit
                    
                    if backtrack(): return True
                    
                    # Backtrack
                    is_uncolored[best_v] = True
                    uncolored.append(best_v)
                    for v2 in adj[best_v]:
                        if is_uncolored[v2]:
                            available[v2] |= color_bit
                            
            return False
        
        return backtrack()

    # Main backtracking function to find lexicographically smallest solution
    def main_backtrack(index):
        if index > n:
            return True
        
        # Try colors 1, 2, 3 in order
        for c in [1, 2, 3]:
            # Check if color c is valid for index (conflict with already colored neighbors)
            # Since we fill ans in order, only neighbors < index are colored
            valid = True
            for v in adj[index]:
                if v < index and ans[v] == c:
                    valid = False
                    break
            
            if valid:
                ans[index] = c
                # Check if the rest of the graph can be colored
                if check_feasible(index + 1, ans):
                    if main_backtrack(index + 1):
                        return True
                ans[index] = 0
        
        return False

    if main_backtrack(1):
        print("YES")
        print(" ".join(map(str, ans[1:])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()