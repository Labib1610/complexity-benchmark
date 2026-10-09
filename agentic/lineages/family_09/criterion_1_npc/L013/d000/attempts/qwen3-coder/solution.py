from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    idx = 3
    conflicts = set()
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        conflicts.add((u, v))
    
    # Generate all combinations of k modules
    modules = list(range(1, n+1))
    for combo in combinations(modules, k):
        # Check if any pair in the combination is conflicting
        valid = True
        for i in range(k):
            for j in range(i+1, k):
                u = combo[i]
                v = combo[j]
                if u > v:
                    u, v = v, u
                if (u, v) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()