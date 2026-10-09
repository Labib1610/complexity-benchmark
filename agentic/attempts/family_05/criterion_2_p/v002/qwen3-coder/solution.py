from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    if t < k:
        print("NO")
        return
    
    # adj[x] will store the list of allowed menus for chef x
    adj = defaultdict(list)
    combos = []
    
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        adj[x].append(z)
        combos.append((x, y, z))
        index += 3
    
    # For each chef, we know his kitchen. 
    # We need to assign each chef to exactly one menu such that:
    # - Each menu is used exactly once
    # - Each chef is used exactly once
    # This is a bipartite matching problem between chefs and menus.
    
    # Build a bipartite graph: chefs -> menus
    # We want a perfect matching (size k)
    
    # Use a standard algorithm for maximum bipartite matching
    # Adjacency list for chefs to menus they can use
    graph = defaultdict(list)
    for x, y, z in combos:
        graph[x].append(z)
    
    # Try to find a maximum matching using DFS-based approach
    match_menu_to_chef = {}  # menu -> chef
    match_chef_to_menu = {}   # chef -> menu
    
    def dfs(chef, visited_menus):
        for menu in graph[chef]:
            if menu in visited_menus:
                continue
            visited_menus.add(menu)
            
            # If menu is unmatched or we can augment the path
            if menu not in match_menu_to_chef:
                match_menu_to_chef[menu] = chef
                match_chef_to_menu[chef] = menu
                return True
            else:
                # Try to rematch the chef who currently has this menu
                other_chef = match_menu_to_chef[menu]
                if dfs(other_chef, visited_menus):
                    match_menu_to_chef[menu] = chef
                    match_chef_to_menu[chef] = menu
                    return True
        return False
    
    matched = 0
    for chef in range(1, k+1):
        visited_menus = set()
        if dfs(chef, visited_menus):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the events
    # We know for each chef what kitchen he uses, and what menu we assigned
    # From input, we can map (chef, menu) back to the full combo
    combo_map = {}
    for x, y, z in combos:
        combo_map[(x, z)] = (x, y, z)
    
    for chef in range(1, k+1):
        menu = match_chef_to_menu[chef]
        print(combo_map[(chef, menu)][0], combo_map[(chef, menu)][1], combo_map[(chef, menu)][2])

solve()