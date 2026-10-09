from collections import defaultdict, deque
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    triads = []
    artifact_to_triads = defaultdict(list)
    
    for i in range(t):
        a = int(data[index]) - 1
        b = int(data[index+1]) - 1
        c = int(data[index+2]) - 1
        index += 3
        triads.append((a, b, c))
        artifact_to_triads[a].append(i)
        artifact_to_triads[b].append(i)
        artifact_to_triads[c].append(i)
    
    # We need to find a perfect matching in a 3-uniform hypergraph
    # This is equivalent to finding a maximum matching that covers all vertices
    # We'll model this as a graph matching problem by creating a node for each triad
    # and connecting triads that share artifacts (since each artifact can only be used once)
    # Actually, let's use backtracking with pruning
    
    total_artifacts = 3 * q
    used_artifacts = [False] * total_artifacts
    selected_triads = []
    result = []
    
    def backtrack(triad_index):
        if len(selected_triads) == q:
            return True
            
        if triad_index == t:
            return False
            
        # Try including current triad if possible
        a, b, c = triads[triad_index]
        if not used_artifacts[a] and not used_artifacts[b] and not used_artifacts[c]:
            used_artifacts[a] = used_artifacts[b] = used_artifacts[c] = True
            selected_triads.append(triad_index)
            if backtrack(triad_index + 1):
                return True
            selected_triads.pop()
            used_artifacts[a] = used_artifacts[b] = used_artifacts[c] = False
            
        # Try skipping current triad
        if backtrack(triad_index + 1):
            return True
            
        return False
    
    # Optimization: sort triads by number of conflicts or use a better search order
    # For now, let's just try the backtracking approach
    if backtrack(0):
        print("YES")
        for idx in selected_triads:
            a, b, c = triads[idx]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    main()