# Phase 3: Drill Deployment Generation

Time limit: 5 s   Memory limit: 256 MB

## Description
The territorial crisis management agency is running its yearly simulation pipeline, which is divided into four stages.

Stage 1 validates the active personnel, outputting a list of field agents with sequential ID codes from $1$ to $3q$. 

Stage 2 filters historical mission logs to produce a catalog of $t$ certified response teams. Each team is strictly composed of three agents who have previously completed joint field certifications. The filtering process guarantees that no ad-hoc groups are included. Additionally, the filtering process enforces two statutory safety margins on every certified team:
- The experience gap (the difference between the highest and lowest agent ID codes in the team) is at most $3q - 1$.
- The combined seniority (the sum of the three agent ID codes) is strictly less than $9q$.

You are responsible for implementing Stage 3. You receive the total number of agents and the catalog of certified teams from Stage 2. Your objective is to formulate a mobilization strategy that activates a specific selection of these teams. The simulation requires full participation: every single agent from the Stage 1 list must be deployed exactly once. Therefore, your strategy must allocate each agent to precisely one activated team, leaving no one behind and ensuring no agent is assigned to multiple teams simultaneously.

If a valid strategy can be formed, it proceeds to Stage 4 for equipment distribution. If it is impossible to incorporate the entire personnel list without overlaps or omissions using the provided catalog, you must report this failure so the simulation can be aborted.

## Input
The first line provides two integers `q` and `t` (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The agency has exactly `3q` agents, with ID codes ranging from 1 to `3q`.
The following `t` lines each describe a certified team from Stage 2. Each line contains three integers `a`, `b`, and `c` (1 ≤ a < b < c ≤ 3q), representing the ID codes of the agents comprising that team.

## Output
If a valid Stage 3 mobilization strategy is possible, output `YES` on the first line. Following this, output `q` lines, each containing the three agent ID codes of an activated team in your strategy.
If no such strategy can be constructed, output `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
