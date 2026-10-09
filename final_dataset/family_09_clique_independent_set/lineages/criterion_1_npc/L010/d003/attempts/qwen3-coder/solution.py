from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # If no locks, any k modules work
    if m == 0:
        print("YES")
        print(' '.join(str(i+1) for i in range(k)))
        return
    
    # Try all combinations of k modules
    for combo in combinations(range(n), k):
        valid = True
        for u, v in edges:
            if u in combo and v in combo:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(str(x+1) for x in combo))
            return
    
    print("NO")

if __name__ == "__main__":
    main()