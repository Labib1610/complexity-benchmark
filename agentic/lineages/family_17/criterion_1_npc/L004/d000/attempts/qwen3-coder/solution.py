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
    # This is essentially a 3D matching problem
    # We can model this as an exact cover problem and use backtracking
    
    # Since q <= 200 and t <= 20000, we need an efficient approach
    # Let's try a greedy approach with backtracking
    
    # Build a graph where each cluster points to reactions that contain it
    cluster_to_reactions = defaultdict(list)
    for i, (a, b, c) in enumerate(reactions):
        cluster_to_reactions[a].append(i)
        cluster_to_reactions[b].append(i)
        cluster_to_reactions[c].append(i)
    
    # Try to find a solution using backtracking
    selected = [False] * t  # which reactions are selected
    used_clusters = [False] * (3*q + 1)  # which clusters are used
    solution = []
    
    def backtrack(pos):
        if pos == 3*q:
            return len(solution) == q
        
        if used_clusters[pos+1]:
            return backtrack(pos+1)
            
        # Try all reactions that contain cluster (pos+1)
        for reaction_idx in cluster_to_reactions[pos+1]:
            if selected[reaction_idx]:
                continue
                
            a, b, c = reactions[reaction_idx]
            if used_clusters[a] or used_clusters[b] or used_clusters[c]:
                continue
                
            # Select this reaction
            selected[reaction_idx] = True
            used_clusters[a] = used_clusters[b] = used_clusters[c] = True
            solution.append(reaction_idx)
            
            if backtrack(pos+1):
                return True
                
            # Backtrack
            selected[reaction_idx] = False
            used_clusters[a] = used_clusters[b] = used_clusters[c] = False
            solution.pop()
            
        return False
    
    # Optimization: start with clusters that have fewer options
    # This can help prune the search space early
    
    # Let's try a different approach: build the solution incrementally
    # and at each step, pick a cluster that hasn't been used yet
    
    def solve():
        selected_reactions = [False] * t
        used = [False] * (3*q + 1)
        result = []
        
        def dfs():
            # Find the first unused cluster
            next_cluster = None
            for i in range(1, 3*q + 1):
                if not used[i]:
                    next_cluster = i
                    break
            
            if next_cluster is None:
                return len(result) == q
            
            # Try all reactions containing this cluster
            for reaction_idx in cluster_to_reactions[next_cluster]:
                if selected_reactions[reaction_idx]:
                    continue
                    
                a, b, c = reactions[reaction_idx]
                if used[a] or used[b] or used[c]:
                    continue
                    
                # Use this reaction
                selected_reactions[reaction_idx] = True
                used[a] = used[b] = used[c] = True
                result.append(reaction_idx)
                
                if dfs():
                    return True
                    
                # Backtrack
                selected_reactions[reaction_idx] = False
                used[a] = used[b] = used[c] = False
                result.pop()
                
            return False
        
        if dfs():
            return [reactions[i] for i in result]
        else:
            return None
    
    result = solve()
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for a, b, c in result:
            print(a, b, c)

if __name__ == "__main__":
    main()