import sys

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    def is_valid(assignment):
        for i in range(1, n + 1):
            color = assignment[i]
            for neighbor in adj[i]:
                if assignment[neighbor] == color:
                    return False
        return True

    def backtrack(index):
        if index > n:
            print("YES")
            print(' '.join(map(str, assignment[1:])))
            sys.exit(0)
        
        for stage in range(1, 4):
            assignment[index] = stage
            if is_valid(assignment):
                backtrack(index + 1)

    assignment = [0] * (n + 1)
    backtrack(1)
    
    print("NO")

if __name__ == "__main__":
    solve()