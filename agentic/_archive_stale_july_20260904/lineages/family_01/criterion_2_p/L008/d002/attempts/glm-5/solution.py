import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Forbidden pairs: (1,1) and (2,2)
    # This is a graph 2-coloring problem
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
    else:
        # color[i] is 0 or 1, we need output 1 or 2
        # Lexicographically smallest: map 0 -> 1, 1 -> 2
        result = [c + 1 for c in color]
        print("YES")
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()