import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        print("NO")
        return
    
    # Now we have a valid bipartition, but we need lexicographically smallest.
    # We can try to flip components if it makes earlier vertices smaller.
    # Since color[0] is 0, we can try to keep as many 1s as possible at the start.
    # But lexicographically smallest means we want 1 at earliest positions.
    # We can do BFS/DFS and for each component, if flipping gives smaller lexicographic order, flip.
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # collect component
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # Check if flipping this component makes lexicographically smaller
            # Compare current vs flipped
            current = [color[u] for u in comp]
            flipped = [1 - color[u] for u in comp]
            # We need to compare based on original indices
            # Sort comp by index to compare properly
            comp_sorted = sorted(comp)
            cur_seq = [color[u] for u in comp_sorted]
            flip_seq = [1 - color[u] for u in comp_sorted]
            if flip_seq < cur_seq:
                for u in comp:
                    color[u] = 1 - color[u]
    
    print("YES")
    print(" ".join(str(color[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()