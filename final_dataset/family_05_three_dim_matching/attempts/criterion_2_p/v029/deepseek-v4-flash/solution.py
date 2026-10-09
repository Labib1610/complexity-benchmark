import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # secondary -> set of tokens
    sec_to_tokens = [set() for _ in range(k)]
    # primary -> secondary mapping (given fixed)
    primary_to_sec = [0] * (k + 1)
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        primary_to_sec[x] = y
        sec_to_tokens[y - 1].add(z)
    
    # Build adjacency: secondary index (0-based) -> list of tokens (1-based)
    adj = [list(tokens) for tokens in sec_to_tokens]
    
    # Matching: token -> secondary assigned
    match_token = [0] * (k + 1)  # 1-based tokens
    
    def dfs(sec, visited):
        for tok in adj[sec]:
            if not visited[tok]:
                visited[tok] = True
                if match_token[tok] == 0 or dfs(match_token[tok] - 1, visited):
                    match_token[tok] = sec + 1
                    return True
        return False
    
    for sec in range(k):
        visited = [False] * (k + 1)
        if not dfs(sec, visited):
            print("NO")
            return
    
    # Build result
    print("YES")
    # For each primary, find its secondary and assigned token
    for x in range(1, k + 1):
        y = primary_to_sec[x]
        # find token assigned to this secondary
        for tok in range(1, k + 1):
            if match_token[tok] == y:
                print(x, y, tok)
                break

if __name__ == "__main__":
    solve()