import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # Check if the subgraph induced by vertices in S is bipartite
    # Returns (is_bipartite, color_array) where color_array is 0 or 1 if bipartite
    def check_bipartite(S):
        if not S:
            return True, {}
        color = {}
        for start_node in S:
            if start_node not in color:
                color[start_node] = 0
                queue = [start_node]
                head = 0
                while head < len(queue):
                    u = queue[head]
                    head += 1
                    for v in S:
                        if adj[u][v]:
                            if v not in color:
                                color[v] = 1 - color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False, {}
        return True, color
    
    # Iterate over all subsets S of vertices to be assigned to shifts 1 and 2
    # The remaining vertices V \ S will be assigned to shift 3
    for mask in range(1 << n):
        S = [i for i in range(n) if (mask >> i) & 1]
        is_bipartite, color = check_bipartite(S)
        if is_bipartite:
            # Found a valid assignment
            res = [3] * n
            for u, c in color.items():
                res[u] = c + 1  # color 0 -> shift 1, color 1 -> shift 2
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, res)) + "\n")
            return
    
    sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()