from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    records = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        records.append((a, b, c))
        index += 3
    
    # Total personnel
    n = 3 * q
    
    # Try to find a matching that covers all nodes exactly once
    # This is essentially a exact cover problem - we can model it as finding a maximum matching
    # But since each record covers 3 people and we need to cover all 3*q people with q records,
    # it's a 3-dimensional matching variant.
    
    # We'll use backtracking with pruning
    # But for efficiency, let's try a different approach: build a graph where each record is a node
    # and there's an edge between two records if they don't share any personnel.
    # Then we need to find a clique of size q in this graph.
    
    # Actually, let's think differently. Build a conflict graph where each record is a node
    # and edges represent conflicts (sharing at least one person).
    # We want to find an independent set of size q.
    
    # But even better approach: direct backtracking with optimization
    # Sort records by some heuristic to try more promising combinations first
    
    # Let's just do a direct backtracking approach with bitmasks for efficiency
    
    # Convert records to sets for faster intersection checking
    record_sets = [set(record) for record in records]
    
    # Which records contain each person
    person_in_records = defaultdict(list)
    for i, record_set in enumerate(record_sets):
        for person in record_set:
            person_in_records[person].append(i)
    
    # Bitmask approach might be too memory intensive for q=200
    # Let's use recursive backtracking with pruning
    
    selected = []
    used_personnel = [False] * (n + 1)
    
    def backtrack(record_idx):
        # If we've selected q records, we're done
        if len(selected) == q:
            return True
            
        # If remaining records can't fill our needs, prune
        if len(selected) + (t - record_idx) < q:
            return False
            
        # Prune if any person is already used more than once (this check is implicit via our logic)
        
        for i in range(record_idx, t):
            record_set = record_sets[i]
            record = records[i]
            
            # Check if this record conflicts with already selected ones
            conflict = False
            for person in record_set:
                if used_personnel[person]:
                    conflict = True
                    break
                    
            if not conflict:
                # Select this record
                selected.append(i)
                for person in record_set:
                    used_personnel[person] = True
                
                # Recurse
                if backtrack(i + 1):
                    return True
                    
                # Backtrack
                selected.pop()
                for person in record_set:
                    used_personnel[person] = False
        
        return False
    
    # Optimization: sort records by how "rare" their elements are
    # Records with rare personnel should be prioritized
    person_count = [0] * (n + 1)
    for record_set in record_sets:
        for person in record_set:
            person_count[person] += 1
    
    # Create list of (record_index, rarity_sum) 
    record_priority = []
    for i, record_set in enumerate(record_sets):
        rarity = sum(person_count[person] for person in record_set)
        record_priority.append((rarity, i))
    
    # Sort by rarity (ascending - rarer elements first)
    record_priority.sort()
    ordered_indices = [idx for _, idx in record_priority]
    
    # Reorder records based on priority
    ordered_records = [records[i] for i in ordered_indices]
    ordered_record_sets = [record_sets[i] for i in ordered_indices]
    
    # Update our structures to use the new ordering
    records = ordered_records
    record_sets = ordered_record_sets
    
    if backtrack(0):
        print("YES")
        for idx in selected:
            record = records[idx]
            print(record[0], record[1], record[2])
    else:
        print("NO")

solve()