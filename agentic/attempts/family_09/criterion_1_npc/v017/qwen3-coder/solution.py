from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read relationships
    relationships = set()
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        relationships.add((min(u, v), max(u, v)))
        index += 2
    
    # Generate all combinations of k candidates
    candidates = list(range(1, n+1))
    for combo in combinations(candidates, k):
        # Check if any pair in the combination has a relationship
        valid = True
        for i in range(k):
            for j in range(i+1, k):
                u = combo[i]
                v = combo[j]
                if (min(u, v), max(u, v)) in relationships:
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