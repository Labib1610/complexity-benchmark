from collections import defaultdict
import sys

def find_matching(k, configs):
    # Create a graph where each mold points to possible (dye, packaging) pairs
    graph = defaultdict(list)
    for x, y, z in configs:
        graph[x].append((y, z))
    
    # For each possible matching, we need to ensure no shared dyes or packaging lines
    # This is essentially finding a perfect matching in a 3D bipartite graph
    # We'll use backtracking with constraint checking
    
    # Precompute available configurations for each mold
    mold_configs = [[] for _ in range(k + 1)]
    for x, y, z in configs:
        mold_configs[x].append((y, z))
    
    # Try to build a solution using backtracking
    def backtrack(mold_idx, used_dyes, used_packaging, selected):
        if mold_idx > k:
            return len(selected) == k
        
        # Try each configuration for this mold
        for y, z in mold_configs[mold_idx]:
            if y not in used_dyes and z not in used_packaging:
                used_dyes.add(y)
                used_packaging.add(z)
                selected.append((mold_idx, y, z))
                
                if backtrack(mold_idx + 1, used_dyes, used_packaging, selected):
                    return True
                
                used_dyes.remove(y)
                used_packaging.remove(z)
                selected.pop()
        
        # Skip this mold (but we must use exactly k configurations)
        # Since we need exactly k, we can't skip if we don't have enough left
        remaining_molds = k - mold_idx
        if len(selected) + remaining_molds >= k:
            if backtrack(mold_idx + 1, used_dyes, used_packaging, selected):
                return True
        
        return False
    
    # Better approach: model as maximum bipartite matching
    # But since we have 3 dimensions, let's think differently
    
    # Create mappings
    # This is actually a tripartite matching problem
    # Let's reduce it to a maximum bipartite matching problem
    
    # For small k (≤ 22), we can try a different approach
    # Try all possible assignments using backtracking more carefully
    
    def solve():
        # Build adjacency for each mold to its possible (dye, pack) pairs
        adj = [None] * (k + 1)
        for i in range(1, k + 1):
            adj[i] = []
            
        for x, y, z in configs:
            adj[x].append((y, z))
        
        # Try to assign each mold to a configuration
        selected = []
        used_dyes = set()
        used_pack = set()
        
        def dfs(mold):
            if mold > k:
                return len(selected) == k
            
            # If we already have enough selected, check if we can complete
            if len(selected) > k:
                return False
                
            # Try each configuration for current mold
            for dye, pack in adj[mold]:
                if dye not in used_dyes and pack not in used_pack:
                    # Try this configuration
                    used_dyes.add(dye)
                    used_pack.add(pack)
                    selected.append((mold, dye, pack))
                    
                    if dfs(mold + 1):
                        return True
                    
                    # Backtrack
                    used_dyes.remove(dye)
                    used_pack.remove(pack)
                    selected.pop()
            
            # If we couldn't find a match for this mold, but we still need to select k,
            # and we've run out of molds, then it's impossible
            return False
        
        # Start with mold 1
        if dfs(1) and len(selected) == k:
            return selected
        return None
    
    # Even better approach: Hungarian algorithm adaptation or direct backtracking
    def backtrack_v2(pos, used_dyes, used_packs, current):
        if len(current) == k:
            return current[:]
        
        if pos > k:
            return None
            
        # Try using this mold
        for dye, pack in mold_configs[pos]:
            if dye not in used_dyes and pack not in used_packs:
                used_dyes.add(dye)
                used_packs.add(pack)
                current.append((pos, dye, pack))
                
                result = backtrack_v2(pos + 1, used_dyes, used_packs, current)
                if result is not None:
                    return result
                
                used_dyes.remove(dye)
                used_packs.remove(pack)
                current.pop()
        
        # Skip this mold
        result = backtrack_v2(pos + 1, used_dyes, used_packs, current)
        return result
    
    result = backtrack_v2(1, set(), set(), [])
    return result

def main():
    input_lines = sys.stdin.read().splitlines()
    line_idx = 0
    
    k, t = map(int, input_lines[line_idx].split())
    line_idx += 1
    
    configs = []
    for _ in range(t):
        x, y, z = map(int, input_lines[line_idx].split())
        configs.append((x, y, z))
        line_idx += 1
    
    # Solve using backtracking with pruning
    # Build a mapping from molds to their configurations
    mold_to_configs = [[] for _ in range(k + 1)]
    for x, y, z in configs:
        mold_to_configs[x].append((y, z))
    
    # Use recursive backtracking
    def search(mold, used_dyes, used_packs, selected):
        if len(selected) == k:
            return selected[:]
        
        if mold > k:
            return None
        
        # Try each configuration for this mold
        for dye, pack in mold_to_configs[mold]:
            if dye not in used_dyes and pack not in used_packs:
                used_dyes.add(dye)
                used_packs.add(pack)
                selected.append((mold, dye, pack))
                
                res = search(mold + 1, used_dyes, used_packs, selected)
                if res is not None:
                    return res
                
                used_dyes.remove(dye)
                used_packs.remove(pack)
                selected.pop()
        
        # Skip this mold
        return search(mold + 1, used_dyes, used_packs, selected)
    
    solution = search(1, set(), set(), [])
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        for x, y, z in solution:
            print(x, y, z)

if __name__ == "__main__":
    main()