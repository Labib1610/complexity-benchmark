from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # For each pair of adjacent nodes u and v,
    # we cannot have f_u + 2*f_v ≡ 0 (mod 3)
    # This is equivalent to f_u ≢ -2*f_v (mod 3)
    # Since -2 ≡ 1 (mod 3), this is f_u ≢ f_v (mod 3)
    # So f_u and f_v cannot be congruent mod 3.
    # That means if f_v ≡ 0, then f_u ≢ 0, etc.
    
    # Actually, let's recheck the condition:
    # f_u + 2*f_v ≡ 0 (mod 3)
    # f_u ≡ -2*f_v ≡ f_v (mod 3)
    # So we cannot have f_u ≡ f_v (mod 3)
    
    # Wait, that's not right either. Let me be more careful:
    # f_u + 2*f_v ≡ 0 (mod 3)
    # f_u ≡ -2*f_v (mod 3)
    # -2 ≡ 1 (mod 3)
    # So f_u ≡ f_v (mod 3)
    
    # No! -2*f_v mod 3:
    # If f_v = 1: -2*1 = -2 ≡ 1 (mod 3), so f_u ≢ 1
    # If f_v = 2: -2*2 = -4 ≡ 2 (mod 3), so f_u ≢ 2  
    # If f_v = 3: -2*3 = -6 ≡ 0 (mod 3), so f_u ≢ 0
    
    # So if f_v = 1, then f_u ≠ 1
    #    if f_v = 2, then f_u ≠ 2
    #    if f_v = 3, then f_u ≠ 3
    # This means f_u ≠ f_v for any adjacent pair.
    
    # Actually, let's double-check with example:
    # f_u = 1, f_v = 2: 1 + 2*2 = 5 ≢ 0 (mod 3)  OK
    # f_u = 1, f_v = 1: 1 + 2*1 = 3 ≡ 0 (mod 3)  BAD
    
    # So indeed f_u ≠ f_v for adjacent nodes.
    # This is a graph coloring problem with 3 colors.
    
    # But wait, the condition is f_u + 2*f_v ≡ 0 (mod 3)
    # Let's be systematic:
    # For f_u + 2*f_v ≡ 0 (mod 3):
    # f_v \ f_u | 1  2  3
    # ----------|--------
    #     1     | 1+2=3  2+2=4≡1  3+2=5≡2   =>  (1,1) is bad
    #     2     | 1+4=5≡2 2+4=6≡0  3+4=7≡1   =>  (2,2) is bad  
    #     3     | 1+6=7≡1 2+6=8≡2  3+6=9≡0   =>  (3,3) is bad
    
    # So indeed, we cannot have f_u = f_v for adjacent nodes.
    
    # This is a 3-coloring problem. We can use backtracking.
    
    # But let's recheck once more:
    # The condition is f_u + 2*f_v ≡ 0 (mod 3)
    # This means f_u ≡ -2*f_v ≡ f_v (mod 3)
    # So we cannot have f_u ≡ f_v (mod 3)
    # Since the values are 1,2,3, this means f_u ≠ f_v.
    
    colors = [0] * (n + 1)  # 0 means uncolored, 1,2,3 are the colors
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()