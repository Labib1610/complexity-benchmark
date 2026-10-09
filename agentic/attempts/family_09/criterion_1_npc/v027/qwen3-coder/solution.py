from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Read interference pairs
    interference = set()
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        interference.add((u, v))
    
    # Generate all combinations of k prototypes
    prototypes = list(range(1, n + 1))
    
    for combo in combinations(prototypes, k):
        # Check if this combination is stable
        is_stable = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if u > v:
                    u, v = v, u
                if (u, v) in interference:
                    is_stable = False
                    break
            if not is_stable:
                break
        
        if is_stable:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()