from collections import defaultdict
import sys

def find_matching(q, t, cases):
    if t < q:
        return None
    
    # Create adjacency list for the tripartite graph
    # Each artifact is a node, each case is a hyperedge connecting 3 nodes
    # We'll use a greedy approach with backtracking
    
    artifacts = list(range(1, 3*q + 1))
    case_list = cases
    
    # Try to find a perfect matching using backtracking
    def backtrack(case_idx, used_artifacts, selected_cases):
        if len(selected_cases) == q:
            return selected_cases[:]
        
        if case_idx >= len(case_list):
            return None
            
        # Try not taking this case
        result = backtrack(case_idx + 1, used_artifacts, selected_cases)
        if result is not None:
            return result
            
        # Try taking this case if none of its artifacts are used
        a, b, c = case_list[case_idx]
        if a not in used_artifacts and b not in used_artifacts and c not in used_artifacts:
            used_artifacts.add(a)
            used_artifacts.add(b)
            used_artifacts.add(c)
            selected_cases.append((a, b, c))
            
            result = backtrack(case_idx + 1, used_artifacts, selected_cases)
            if result is not None:
                return result
                
            selected_cases.pop()
            used_artifacts.remove(a)
            used_artifacts.remove(b)
            used_artifacts.remove(c)
            
        return None
    
    # Optimization: if an artifact appears in only one case, that case must be selected
    artifact_count = defaultdict(int)
    artifact_cases = defaultdict(list)
    
    for i, (a, b, c) in enumerate(case_list):
        artifact_count[a] += 1
        artifact_count[b] += 1
        artifact_count[c] += 1
        artifact_cases[a].append(i)
        artifact_cases[b].append(i)
        artifact_cases[c].append(i)
    
    # Check if any artifact appears in 0 cases
    for artifact in artifacts:
        if artifact_count[artifact] == 0:
            return None
    
    mandatory_cases = set()
    for artifact in artifacts:
        if artifact_count[artifact] == 1:
            case_idx = artifact_cases[artifact][0]
            mandatory_cases.add(case_idx)
    
    # If we have more mandatory cases than needed, impossible
    if len(mandatory_cases) > q:
        return None
    
    # Pre-select mandatory cases
    preselected = []
    used = set()
    
    for case_idx in mandatory_cases:
        a, b, c = case_list[case_idx]
        if a in used or b in used or c in used:
            return None  # Conflict in mandatory cases
        preselected.append((a, b, c))
        used.add(a)
        used.add(b)
        used.add(c)
    
    # Filter remaining cases to only those with unused artifacts
    remaining_cases = []
    for i, (a, b, c) in enumerate(case_list):
        if i not in mandatory_cases:
            remaining_cases.append((a, b, c))
    
    # Now solve the reduced problem
    def solve_remaining(cases_to_check, target_count):
        if target_count == 0:
            return []
            
        if len(cases_to_check) < target_count:
            return None
            
        def bt(idx, curr_used, selected):
            if len(selected) == target_count:
                return selected[:]
            
            if idx >= len(cases_to_check):
                return None
                
            # Pruning: if not enough cases left
            if len(selected) + (len(cases_to_check) - idx) < target_count:
                return None
            
            # Try not taking current case
            res = bt(idx + 1, curr_used, selected)
            if res is not None:
                return res
            
            # Try taking current case
            a, b, c = cases_to_check[idx]
            if a not in curr_used and b not in curr_used and c not in curr_used:
                curr_used.add(a)
                curr_used.add(b)
                curr_used.add(c)
                selected.append((a, b, c))
                
                res = bt(idx + 1, curr_used, selected)
                if res is not None:
                    return res
                    
                selected.pop()
                curr_used.remove(a)
                curr_used.remove(b)
                curr_used.remove(c)
            
            return None
        
        return bt(0, set(), [])
    
    remaining_result = solve_remaining(remaining_cases, q - len(preselected))
    if remaining_result is not None:
        return preselected + remaining_result
    
    return None

# Read input
line = input().split()
q, t = int(line[0]), int(line[1])

cases = []
for _ in range(t):
    line = input().split()
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    cases.append((a, b, c))

result = find_matching(q, t, cases)

if result is None:
    print("NO")
else:
    print("YES")
    for case in result:
        print(case[0], case[1], case[2])