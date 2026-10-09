import sys
from collections import defaultdict

def solve():
    q, t = map(int, sys.stdin.readline().split())
    triplets = []
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        triplets.append((a, b, c))
    
    # Build a mapping from each page to the list of triplets containing it
    page_to_triplets = defaultdict(list)
    for i, (a, b, c) in enumerate(triplets):
        page_to_triplets[a].append(i)
        page_to_triplets[b].append(i)
        page_to_triplets[c].append(i)
    
    # Try to build a solution using backtracking with pruning
    selected = []
    used_pages = [False] * (3*q + 1)
    
    def backtrack(page_index):
        # If we've processed all pages, check if we have exactly q triplets
        if page_index > 3*q:
            return len(selected) == q
        
        # If this page is already used, move to the next one
        if used_pages[page_index]:
            return backtrack(page_index + 1)
        
        # Try each triplet that contains this page (as the smallest element)
        for triplet_idx in page_to_triplets[page_index]:
            a, b, c = triplets[triplet_idx]
            # Check if this is a valid choice (a must be page_index and b,c must be unused)
            if a == page_index and not used_pages[b] and not used_pages[c]:
                # Make the choice
                selected.append(triplet_idx)
                used_pages[a] = True
                used_pages[b] = True
                used_pages[c] = True
                
                # Recurse
                if backtrack(page_index + 1):
                    return True
                
                # Backtrack
                selected.pop()
                used_pages[a] = False
                used_pages[b] = False
                used_pages[c] = False
        
        return False
    
    # Start backtracking from page 1
    if backtrack(1):
        print("YES")
        for idx in selected:
            a, b, c = triplets[idx]
            print(a, b, c)
    else:
        print("NO")

solve()