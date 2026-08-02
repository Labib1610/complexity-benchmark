def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    incompat_prev = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        a = min(u, v)
        b = max(u, v)
        incompat_prev[b].append(a)
    
    shifts = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for s in [1, 2, 3]:
            conflict = False
            for j in incompat_prev[i]:
                if shifts[j] == s:
                    conflict = True
                    break
            if not conflict:
                shifts[i] = s
                break
        else:
            print("IMPOSSIBLE")
            return
    
    print(' '.join(map(str, shifts[1:n+1])))

if __name__ == "__main__":
    main()