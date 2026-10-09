from itertools import combinations
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Create adjacency list to represent reactive pairs
    reactive = set()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        reactive.add((min(u, v), max(u, v)))
    
    # Generate all possible combinations of k substances
    substances = list(range(1, n + 1))
    
    # Check each combination
    for combo in combinations(substances, k):
        # Check if this combination is stable
        is_stable = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if (min(u, v), max(u, v)) in reactive:
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