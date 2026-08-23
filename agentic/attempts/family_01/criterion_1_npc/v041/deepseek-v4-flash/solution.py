import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    # Try to assign colors 1,2,3 in lexicographic order
    def backtrack(person):
        if person == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[person]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[person] = c
                if backtrack(person + 1):
                    return True
                color[person] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()