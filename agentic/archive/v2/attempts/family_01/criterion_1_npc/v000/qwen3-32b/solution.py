def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    def backtrack(pos):
        if pos > n:
            return True
        for c in [1, 2, 3]:
            valid = True
            for neighbor in adj[pos]:
                if neighbor < pos and color[neighbor] == c:
                    valid = False
                    break
            if valid:
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = 0
        return False
    
    if backtrack(1):
        print(' '.join(map(str, color[1:])))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()