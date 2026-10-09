from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    reactions = []
    index = 2
    for i in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        reactions.append((a, b, c))
        index += 3
    
    # We need to find a perfect matching that covers all 3q nodes
    # This is equivalent to finding a exact cover problem
    # We can model this as a bipartite matching or use backtracking with pruning
    
    # Since q <= 200 and t <= 20000, we should use a more efficient approach
    # Let's try to model this as an exact cover problem and solve with backtracking + optimizations
    
    # Each cluster from 1 to 3*q must be covered exactly once
    # Each reaction covers exactly 3 clusters
    
    # Use backtracking with bitmasks for efficiency
    
    # First, let's map each cluster to the list of reactions that contain it
    cluster_to_reactions = defaultdict(list)
    for idx, (a, b, c) in enumerate(reactions):
        cluster_to_reactions[a].append(idx)
        cluster_to_reactions[b].append(idx)
        cluster_to_reactions[c].append(idx)
    
    # We'll use a recursive backtracking approach
    selected = []
    used_reactions = [False] * t
    covered_clusters = [False] * (3*q + 1)
    
    def backtrack():
        # Find the first uncovered cluster
        next_cluster = -1
        for i in range(1, 3*q + 1):
            if not covered_clusters[i]:
                next_cluster = i
                break
        
        # If all clusters are covered, we found a solution
        if next_cluster == -1:
            return len(selected) == q
        
        # Try all reactions that contain next_cluster
        for reaction_idx in cluster_to_reactions[next_cluster]:
            if used_reactions[reaction_idx]:
                continue
            
            a, b, c = reactions[reaction_idx]
            
            # Check if all clusters of this reaction are free
            if covered_clusters[a] or covered_clusters[b] or covered_clusters[c]:
                continue
            
            # Use this reaction
            selected.append(reaction_idx)
            used_reactions[reaction_idx] = True
            covered_clusters[a] = True
            covered_clusters[b] = True
            covered_clusters[c] = True
            
            # Recurse
            if backtrack():
                return True
            
            # Backtrack
            selected.pop()
            used_reactions[reaction_idx] = False
            covered_clusters[a] = False
            covered_clusters[b] = False
            covered_clusters[c] = False
        
        return False
    
    # Optimization: if any cluster is not part of any reaction, return NO
    for i in range(1, 3*q + 1):
        if not cluster_to_reactions[i]:
            print("NO")
            return
    
    if backtrack():
        print("YES")
        for reaction_idx in selected:
            a, b, c = reactions[reaction_idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()