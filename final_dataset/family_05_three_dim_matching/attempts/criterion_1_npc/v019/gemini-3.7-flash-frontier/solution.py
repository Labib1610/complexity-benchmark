import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    # Each triple is 0-indexed: x in [0, k-1], y in [0, k-1], z in [0, k-1]
    # We can model this as an exact cover problem with 3k items.
    # Item 0..k-1: Shape
    # Item k..2k-1: Color
    # Item 2k..3k-1: Material
    
    options = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        options.append((x, y, z))
    
    # Store options containing each item
    item_options = [[] for _ in range(3 * k)]
    for opt_id, (x, y, z) in enumerate(options):
        item_options[x].append(opt_id)
        item_options[k + y].append(opt_id)
        item_options[2 * k + z].append(opt_id)
        
    # Quick feasibility check: every item must appear at least once
    for i in range(3 * k):
        if not item_options[i]:
            print("NO")
            return

    # Backtracking with MRV and degree-based item selection
    # active_items: set of items not yet covered
    # active_options: boolean array indicating which options are still candidate
    
    active_options = [True] * len(options)
    
    # For fast lookup of items covered by an option
    opt_items = []
    for x, y, z in options:
        opt_items.append((x, k + y, 2 * k + z))
        
    solution = []
    
    def search(num_chosen):
        if num_chosen == k:
            return True
        
        # Find item with minimum remaining candidates
        best_item = -1
        min_candidates = 1000000
        best_cand_list = None
        
        for item in range(3 * k):
            if item_covered[item]:
                continue
            
            # Count valid options for this item
            cand_count = 0
            cand_list = []
            for opt_id in item_options[item]:
                if active_options[opt_id]:
                    cand_count += 1
                    cand_list.append(opt_id)
                    
            if cand_count == 0:
                return False
            
            if cand_count < min_candidates:
                min_candidates = cand_count
                best_item = item
                best_cand_list = cand_list
                if min_candidates == 1:
                    break
        
        # Branch on the chosen item's valid options
        for opt_id in best_cand_list:
            if not active_options[opt_id]:
                continue
            
            # Cover this option
            solution.append(opt_id)
            disabled_options = []
            items_to_cover = opt_items[opt_id]
            
            for it in items_to_cover:
                item_covered[it] = True
                for conf_opt in item_options[it]:
                    if active_options[conf_opt]:
                        active_options[conf_opt] = False
                        disabled_options.append(conf_opt)
            
            if search(num_chosen + 1):
                return True
            
            # Backtrack
            solution.pop()
            for it in items_to_cover:
                item_covered[it] = False
            for dis_opt in disabled_options:
                active_options[dis_opt] = True
                
        return False

    item_covered = [False] * (3 * k)
    
    if search(0):
        print("YES")
        out = []
        for opt_id in solution:
            x, y, z = options[opt_id]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()