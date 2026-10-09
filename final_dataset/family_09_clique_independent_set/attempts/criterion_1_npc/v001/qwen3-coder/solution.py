from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read edges
    edges = set()
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        # Store edges in sorted order to avoid duplication
        edges.add((min(u, v), max(u, v)))
    
    # Generate all combinations of k nodes
    nodes = list(range(1, n+1))
    for combo in combinations(nodes, k):
        # Check if this combination is interference-free
        valid = True
        for i in range(k):
            for j in range(i+1, k):
                u = combo[i]
                v = combo[j]
                if (min(u, v), max(u, v)) in edges:
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