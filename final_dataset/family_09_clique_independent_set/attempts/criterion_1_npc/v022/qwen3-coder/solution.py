from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # If k == 1, just pick any plugin
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For small n, try all combinations
    if n <= 20:
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
        return
    
    # For larger n, use greedy + local search
    # Greedy: start with empty set, add nodes with smallest degree
    nodes = list(range(n))
    nodes.sort(key=lambda x: len(adj[x]))
    
    selected = []
    selected_set = set()
    
    for node in nodes:
        # Check if we can add this node
        conflict = False
        for neighbor in adj[node]:
            if neighbor in selected_set:
                conflict = True
                break
        if not conflict:
            selected.append(node)
            selected_set.add(node)
            if len(selected) == k:
                print("YES")
                print(' '.join(str(x+1) for x in selected))
                return
    
    # If greedy didn't work, try random restarts
    import random
    random.seed(42)
    
    for _ in range(1000):
        # Try a random subset
        candidate = random.sample(range(n), min(k, n))
        candidate_set = set(candidate)
        valid = True
        for u, v in edges:
            if u in candidate_set and v in candidate_set:
                valid = False
                break
        if valid and len(candidate) >= k:
            # Trim to size k if needed
            if len(candidate) > k:
                candidate = candidate[:k]
            elif len(candidate) < k:
                # Extend carefully
                added = len(candidate)
                for i in range(n):
                    if i not in candidate_set:
                        conflict = False
                        for neighbor in adj[i]:
                            if neighbor in candidate_set:
                                conflict = True
                                break
                        if not conflict:
                            candidate.append(i)
                            candidate_set.add(i)
                            added += 1
                            if added == k:
                                break
            if len(candidate) == k:
                print("YES")
                print(' '.join(str(x+1) for x in candidate))
                return
    
    print("NO")

if __name__ == "__main__":
    main()