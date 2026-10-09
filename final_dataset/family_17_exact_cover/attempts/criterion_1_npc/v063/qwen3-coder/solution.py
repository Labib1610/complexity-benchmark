from collections import defaultdict
import sys

def solve():
    q, t = map(int, input().split())
    teams = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        teams.append((a, b, c))
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    # Build graph: each person is connected to teams they belong to
    person_to_teams = defaultdict(list)
    team_adj = [[] for _ in range(t)]
    
    for i, (a, b, c) in enumerate(teams):
        person_to_teams[a].append(i)
        person_to_teams[b].append(i)
        person_to_teams[c].append(i)
    
    # Build adjacency list for teams that share persons
    for i, (a, b, c) in enumerate(teams):
        for person in [a, b, c]:
            for j in person_to_teams[person]:
                if i != j:
                    team_adj[i].append(j)
    
    # Try to find a matching that covers all 3*q persons
    # This is essentially a maximum matching problem in a hypergraph
    # But we can model it as finding a perfect matching in a graph where
    # nodes are teams and edges represent compatibility (no shared persons)
    
    # Two teams are compatible if they don't share any person
    def are_compatible(i, j):
        team_i = set(teams[i])
        team_j = set(teams[j])
        return len(team_i.intersection(team_j)) == 0
    
    # Build compatibility graph
    compat_graph = [[] for _ in range(t)]
    for i in range(t):
        for j in range(i+1, t):
            if are_compatible(i, j):
                compat_graph[i].append(j)
                compat_graph[j].append(i)
    
    # Find maximum matching using backtracking with pruning
    selected_teams = []
    used_persons = set()
    
    def backtrack(index):
        if len(selected_teams) == q:
            return True
        
        if index >= t:
            return False
            
        # Pruning: if even selecting all remaining teams won't give us enough
        if len(selected_teams) + (t - index) < q:
            return False
            
        # Try including current team
        team = teams[index]
        team_set = set(team)
        
        if not (team_set & used_persons):  # No person conflict
            selected_teams.append(index)
            used_persons.update(team_set)
            
            if backtrack(index + 1):
                return True
                
            selected_teams.pop()
            used_persons.difference_update(team_set)
        
        # Try not including current team
        if backtrack(index + 1):
            return True
            
        return False
    
    if backtrack(0):
        print("YES")
        for idx in selected_teams:
            team = teams[idx]
            print(team[0], team[1], team[2])
    else:
        print("NO")

solve()