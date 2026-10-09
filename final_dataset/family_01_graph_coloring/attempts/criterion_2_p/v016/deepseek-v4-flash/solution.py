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
    comps = []
    
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            comp = []
            is_bip = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bip = False
            if not is_bip:
                print("NO")
                return
            comps.append(comp)
    
    ans = [0] * n
    for comp in comps:
        # comp contains vertices with colors 0 or 1
        # We can either keep as is or flip
        # Choose orientation that gives lexicographically smaller
        # Compare the two possibilities
        # Option 1: color 0 -> 1, color 1 -> 2
        # Option 2: color 0 -> 2, color 1 -> 1
        # We compare by the smallest index in comp
        min_idx = min(comp)
        # If min_idx has color 0, option1 gives 1, option2 gives 2 -> option1 smaller
        # If min_idx has color 1, option1 gives 2, option2 gives 1 -> option2 smaller
        if color[min_idx] == 0:
            for u in comp:
                ans[u] = 1 if color[u] == 0 else 2
        else:
            for u in comp:
                ans[u] = 2 if color[u] == 0 else 1
    
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()