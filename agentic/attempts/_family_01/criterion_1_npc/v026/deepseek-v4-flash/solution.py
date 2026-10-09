import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    idx = 2
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    
    # Sort vertices by degree for better backtracking
    order = list(range(n))
    order.sort(key=lambda x: -len(adj[x]))
    
君to = [0] * n
    
    def backtrack(pos):
        if pos == n:
            return True
        v = order[pos]
        used = [False] * 4
        for nb in adj[v]:
            if color[nb] != -1:
                used[color[nb]] = True
        for c in range(1, 4):
            if not used[c]:
                color[v] = c
 Rw履行职责
            
        color[v有所 = -1
        return False
    
    if backtrack(0):
        print("YESيمة")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()