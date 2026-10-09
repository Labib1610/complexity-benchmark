import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u][v] = adj[v][u] = True

    # Check if a pair (a,b) is allowed
    def ok(a, b):
        if a > b:
            a, b = b, a
        return a * a + b * b > 3 * a * a

    # Try all 3^n assignments (n <= 40 too large, but we can use backtracking with pruning)
    # Since n <= 40, we can use meet-in-the-middle or backtracking with pruning.
    # But 3^40 is too large. However, the constraint is small enough for a backtracking with pruning?
    # Actually, we can use the fact that the condition only depends on the smaller value.
    # Let's try a different approach: try all assignments of 1,2,3 to vertices, but prune.
    # Since n <= 40, we can use backtracking with forward checking.
    
    # Let's just try all possibilities for the first few vertices and use backtracking.
    # But worst-case 3^40 is too large. However, the problem is from a contest and likely has a solution using 2-SAT or graph coloring.
    # Let's analyze the condition:
    # For a pair (a,b) with a <= b, condition: a^2 + b^2 > 3a^2 => b^2 > 2a^2 => b > sqrt(2)*a.
    # So if a=1, need b > sqrt(2) => b >= 2.
    # If a=2, need b > 2*sqrt(2) => b >= 3.
    # If a=3, need b > 3*sqrt(2) => b >= 5, impossible.
    # So no edge can have both endpoints with value 3, and no edge can have (2,2) or (1,1) or (1,2) or (2,3) or (3,3).
    # Allowed pairs: (1,2), (1,3), (2,3) are allowed? Check:
    # (1,2): 1+4=5 > 3*1=3 OK
    # (1,3): 1+9=10 > 3*1=3 OK
    # (2,3): 4+9=13 > 3*4=12 OK
    # So the only forbidden pairs are (1,1), (2,2), (3,3), (1,2)? Wait check (1,2): 1+4=5 > 3*1=3 OK.
    # Actually (1,2) is allowed. Let's list all pairs:
    # (1,1): 1+1=2 > 3*1=3? No.
    # (1,2): 1+4=5 > 3*1=3? Yes.
    # (1,3): 1+9=10 > 3*1=3? Yes.
    # (2,2): 4+4=8 > 3*4=12? No.
    # (2,3): 4+9=13 > 3*4=12? Yes.
    # (3,3): 9+9=18 > 3*9=27? No.
    # So forbidden pairs: (1,1), (2,2), (3,3), (2,3) and (3,2) and (3,3) already counted.
    # Wait (2,3) is allowed? 4+9=13 > 12 yes.
    # So only forbidden are (1,1), (2,2), (3,3).
    # So the condition is simply that no edge can have both endpoints with the same value.
    # Because if a=b, then 2a^2 > 3a^2 => 0 > a^2, impossible.
    # If a != b, then a^2 + b^2 > 3*min(a,b)^2. Since min is at most 2, and the other is at least 2, it's always true.
    # Let's verify: if a=1,b=2: 1+4=5 > 3*1=3 OK. a=1,b=3: 1+9=10 > 3 OK. a=2,b=3: 4+9=13 > 12 OK.
    # So the problem reduces to: can we color the graph with 3 colors such that no edge has both endpoints the same color?
    # That's exactly 3-coloring, which is NP-complete in general, but n <= 40, so we can use backtracking with pruning.
    # Since 3^40 is too large, but we can use the fact that the graph might be sparse or use bitmask DP? No.
    # Actually, 3-coloring is NP-complete, but n=40 is small enough for backtracking with pruning in practice? Possibly not in worst case.
    # But the problem likely expects a solution using the fact that the graph must be bipartite? No, 3-coloring is not just bipartite.
    # Wait, the condition is that no edge can have the same color. So it's exactly a proper 3-coloring.
    # For n=40, we can use backtracking with forward checking and choose the vertex with the most constraints (MRV heuristic).
    # This should pass within time limit for n=40.
    
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    color = [-1] * n
    
    # Check if we can color vertex v with color c
    def is_safe(v, c):
        for u in adj_list[v]:
            if color[u] == c:
                return False
        return True
    
    # Backtracking with MRV
    def backtrack():
        # Find uncolored vertex with most colored neighbors (or smallest domain)
        v = -1
        best = -1
        for i in range(n):
            if color[i] == -1:
                # count available colors
                avail = 0
                for c in range(3):
                    if is_safe(i, c):
                        avail += 1
                if avail > best:
                    best = avail
                    v = i
                    if best == 0:
                        return False
        if v == -1:
            return True
        # Try colors in order
        for c in range(3):
            if is_safe(v, c):
                color[v] = c
                if backtrack():
                    return True
                color[v] = -1
        return False
    
    if backtrack():
        print("YES")
        print(' '.join(str(c+1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()