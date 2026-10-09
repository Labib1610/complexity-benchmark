import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    degree = [0] * n
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v and not ((adj[u] >> v) & 1):
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            degree[u] += 1
            degree[v] += 1

    color = [-1] * n
    sat = [0] * n  # bitmask of neighbor colors
    
    # DSatur backtracking
    def get_next_vertex():
        best_v = -1
        max_sat_count = -1
        max_deg = -1
        for i in range(n):
            if color[i] == -1:
                sat_count = bin(sat[i]).count('1')
                if sat_count > max_sat_count:
                    max_sat_count = sat_count
                    max_deg = degree[i]
                    best_v = i
                elif sat_count == max_sat_count:
                    if degree[i] > max_deg:
                        max_deg = degree[i]
                        best_v = i
        return best_v

    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        u = get_next_vertex()
        if u == -1:
            return True
        
        used_colors = sat[u]
        # Try available colors among {0, 1, 2}
        for c in range(3):
            if not ((used_colors >> c) & 1):
                color[u] = c
                # Update sat for uncolored neighbors
                updated = []
                mask = adj[u]
                while mask:
                    lsb = mask & -mask
                    v = (lsb).bit_length() - 1
                    mask ^= lsb
                    if color[v] == -1:
                        if not ((sat[v] >> c) & 1):
                            sat[v] |= (1 << c)
                            updated.append(v)
                
                # Check if any neighbor is now impossible (saturation == 7, i.e., all 3 colors used)
                possible = True
                for v in updated:
                    if sat[v] == 7:
                        possible = False
                        break
                
                if possible and backtrack(assigned_count + 1):
                    return True
                
                # Revert
                for v in updated:
                    sat[v] &= ~(1 << c)
                color[u] = -1
                
        return False

    if backtrack(0):
        print("YES")
        print(*(c + 1 for c in color))
    else:
        print("NO")

if __name__ == '__main__':
    solve()