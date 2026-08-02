def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Preprocess: store only neighbors with smaller indices
    adj_less = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for neighbor in adj[i]:
            if neighbor < i:
                adj_less[i].append(neighbor)
    
    color = [0] * (n + 1)
    
    def backtrack(i):
        if i > n:
            return True
        for c in [1, 2, 3]:
            valid = True
            for neighbor in adj_less[i]:
                if color[neighbor] == c:
                    valid = False
                    break
            if not valid:
                continue
            color[i] = c
            if backtrack(i + 1):
                return True
            color[i] = 0
        return False
    
    if backtrack(1):
        print("Yes")
        print(' '.join(map(str, color[1:])))
    else:
        print("No")

if __name__ == "__main__":
    main()