from itertools import combinations
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Read interference pairs
    interference = set()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        interference.add((u, v))
    
    # Generate all possible combinations of k markers
    markers = list(range(1, n + 1))
    
    for combo in combinations(markers, k):
        # Check if this combination is valid
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if u > v:
                    u, v = v, u
                if (u, v) in interference:
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