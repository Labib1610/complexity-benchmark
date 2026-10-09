from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    recipes = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        recipes.append((a, b, c))
        index += 3
    
    # Build graph for matching
    # Each precursor is a node on the left (0 to 3*q-1)
    # Each recipe is a node on the right (3*q to 3*q + t - 1)
    # Edges connect precursors to recipes that use them
    
    # We model this as a matching problem:
    # Find a perfect matching from precursors to recipes (each recipe covers 3 precursors)
    
    # This is essentially a exact cover problem. We can solve it with backtracking.
    
    # Use backtracking with pruning
    total_precursors = 3 * q
    precursor_list = list(range(1, total_precursors + 1))
    
    # For each precursor, keep track of which recipes use it
    recipes_for_precursor = defaultdict(list)
    for i, (a, b, c) in enumerate(recipes):
        recipes_for_precursor[a].append(i)
        recipes_for_precursor[b].append(i)
        recipes_for_precursor[c].append(i)
    
    # Sort recipes by the smallest precursor number to heuristically improve search
    # Not necessary but might help
    
    selected = [False] * t  # which recipes are selected
    result = []
    found = False
    
    def backtrack(precursor_index):
        nonlocal found
        if found:
            return
        if precursor_index == total_precursors:
            found = True
            return
            
        current_precursor = precursor_list[precursor_index]
        
        # Try all recipes that contain this precursor and are not yet selected
        for recipe_idx in recipes_for_precursor[current_precursor]:
            if selected[recipe_idx]:
                continue
            a, b, c = recipes[recipe_idx]
            # Check if all precursors in this recipe are available (not yet assigned)
            # Since we process precursors in order, and each recipe has 3 precursors,
            # we need to make sure none of a,b,c have been processed yet
            # But since we're going in order, and a<b<c, if we're at 'a', then b and c are not processed
            # However, we still need to ensure that when we process b and c later, this recipe is already selected
            # Actually, let's think differently.
            
            # Let's sort the precursor list and assign recipes such that each recipe is picked when its first element is encountered
            
            # Even better approach: when we encounter the first element of a recipe, we decide whether to pick it
            # But we need to make sure that picking it doesn't conflict with previous decisions
            
            # Let's try a different backtracking: for each precursor in order, if it's not yet covered, 
            # we must pick a recipe that includes it. 
            
            # But to make it efficient, when we process precursor in order, and we see one that's not covered,
            # we try all recipes that include it and haven't been selected.
            
            # To track which precursors are covered, we can have a boolean array
            pass
        
    # Let's reframe:
    # We want to select exactly q recipes such that every precursor from 1 to 3q appears exactly once
    # This is a exact cover problem
    
    # Use a recursive backtracking approach
    used_precursors = [False] * (total_precursors + 1)  # 1-indexed
    selected_recipes = []
    solution = None
    
    def solve(recipe_index):
        nonlocal solution
        if solution is not None:
            return
            
        # Count how many precursors are used
        count = sum(used_precursors)
        if count == total_precursors:
            solution = selected_recipes[:]
            return
            
        if recipe_index == t:
            return
            
        # Pruning: if even if we select all remaining recipes, we won't have enough
        max_possible = len(selected_recipes) + (t - recipe_index)
        if max_possible < q:
            return
            
        # Option 1: Skip current recipe
        solve(recipe_index + 1)
        
        # Option 2: Take current recipe, if possible
        a, b, c = recipes[recipe_index]
        if not used_precursors[a] and not used_precursors[b] and not used_precursors[c]:
            # Take the recipe
            used_precursors[a] = used_precursors[b] = used_precursors[c] = True
            selected_recipes.append(recipe_index)
            solve(recipe_index + 1)
            if solution is not None:
                return
            # Backtrack
            used_precursors[a] = used_precursors[b] = used_precursors[c] = False
            selected_recipes.pop()
    
    # Optimization: preprocess to only consider relevant recipes
    # But let's just run the backtracking
    solve(0)
    
    if solution is None:
        print("NO")
    else:
        print("YES")
        for idx in solution:
            a, b, c = recipes[idx]
            print(a, b, c)

if __name__ == "__main__":
    main()