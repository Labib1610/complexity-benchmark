def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    shifts = [0] * (n + 1)
    
    for u in range(1, n + 1):
        for s in [1, 2, 3]:
            conflict = False
            for v in adj[u]:
                if v < u:
                    if shifts[v] == s:
                        conflict = True
                        break
            if not conflict:
                shifts[u] = s
                break
        if shifts[u] == 0:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, shifts[1:])))

if __name__ == "__main__":
    main()