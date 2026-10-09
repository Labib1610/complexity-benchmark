import sys

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # chef_menus[chef] = list of menus allowed
    chef_menus = [[] for _ in range(k + 1)]
    chef_kitchen = [0] * (k + 1)
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        chef_menus[x].append(z)
        chef_kitchen[x] = y  # fixed kitchen for chef
    
    # Kuhn's algorithm for bipartite matching
    match_menu = [0] * (k + 1)  # match_menu[menu] = chef
    visited = [False] * (k + 1)
    
    def dfs(chef):
        for menu in chef_menus[chef]:
            if visited[menu]:
                continue
            visited[menu] = True
            if match_menu[menu] == 0 or dfs(match_menu[menu]):
                match_menu[menu] = chef
                return True
        return False
    
    match_count = 0
    for chef in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(chef):
            match_count += 1
    
    if match_count == k:
        print("YES")
        for menu in range(1, k + 1):
            chef = match_menu[menu]
            print(chef, chef_kitchen[chef], menu)
    else:
        print("NO")

if __name__ == "__main__":
    main()