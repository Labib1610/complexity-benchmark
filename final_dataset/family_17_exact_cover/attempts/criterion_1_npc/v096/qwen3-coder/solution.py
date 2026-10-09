from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    num_agents = 3 * q
    
    teams = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        teams.append((a, b, c))
        index += 3
    
    # Build a graph: for each agent, list of teams that contain this agent
    agent_teams = defaultdict(list)
    for idx, (a, b, c) in enumerate(teams):
        agent_teams[a].append(idx)
        agent_teams[b].append(idx)
        agent_teams[c].append(idx)
    
    # Try to find a matching that covers all agents
    # This is essentially a maximum matching problem in a 3-uniform hypergraph,
    # but we can model it as a graph matching problem by creating a node for each team
    # and trying to find a set of teams such that each agent appears in exactly one team.
    
    # We'll use backtracking / recursive search with pruning
    
    def can_match(agent, team_match, matched_agents, team_used):
        # Try to assign teams to agents starting from 'agent'
        if agent > num_agents:
            return True
        
        if matched_agents[agent]:
            return can_match(agent + 1, team_match, matched_agents, team_used)
        
        # Try all teams containing this agent
        for team_idx in agent_teams[agent]:
            if team_used[team_idx]:
                continue
            a, b, c = teams[team_idx]
            if matched_agents[a] or matched_agents[b] or matched_agents[c]:
                continue
            
            # Assign this team
            team_match.append(team_idx)
            team_used[team_idx] = True
            matched_agents[a] = True
            matched_agents[b] = True
            matched_agents[c] = True
            
            if can_match(agent + 1, team_match, matched_agents, team_used):
                return True
            
            # Backtrack
            team_match.pop()
            team_used[team_idx] = False
            matched_agents[a] = False
            matched_agents[b] = False
            matched_agents[c] = False
        
        return False
    
    # Optimization: sort agents and try to match in order
    # Start with agent 1
    team_match = []
    matched_agents = [False] * (num_agents + 1)  # 1-based indexing
    team_used = [False] * t
    
    if can_match(1, team_match, matched_agents, team_used):
        print("YES")
        for idx in team_match:
            a, b, c = teams[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()