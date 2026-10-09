# Problem A — Post-Incident Containment Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
The facility's emergency management system operates in three automated phases following a hazardous materials breach. You are responsible for implementing the control logic for Phase 2. 

**Phase 1: Diagnostic Scan (Completed)**
The system has mapped the facility, which consists of a network of sectors connected by transit shafts. Telemetry has identified $k$ specific sectors, designated as *hubs*, where incompatible reactive agents have been exposed. 

**Phase 2: Quarantine Execution (Your Task)**
The automated protocol must isolate these reactive agents from one another to prevent catastrophic mixing. This is achieved by deploying heavy blast doors in a chosen set of transit shafts. Each shaft requires a specific amount of reserve power to seal, and once sealed, neither personnel nor materials can pass through it in either direction. The facility has a strict reserve power limit. 

Your objective is to select a set of shafts to seal such that the total power required does not exceed the power limit, and no two hubs have any remaining sequence of unsealed shafts connecting them. Sectors that are not hubs will naturally end up partitioned into these separated zones; their final placement does not matter as long as every hub is completely separated from every other hub. 

**Phase 3: Sterilization (Pending)**
Once Phase 2 confirms successful isolation, decontamination crews and drones will be deployed into the separated regions to neutralize the agents. This phase cannot begin until you guarantee the hubs are mutually isolated.

Given the facility layout and the available power, determine if a valid deployment of blast doors exists within the budget, and if so, specify which shafts to seal. (While separating any single pair of hubs might require little power, your single set of chosen shafts must simultaneously separate all hubs from one another without exceeding the total power limit).

## Input
The first line contains four integers $n$ (the total number of sectors), $m$ (the total number of shafts), $k$ (the number of hubs), and $B$ (the reserve power limit).
The second line contains $k$ integers representing the IDs of the hub sectors.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a shaft between sector $u$ and sector $v$ that requires $w$ units of power to seal.

## Output
If Phase 2 isolation is possible within the power limit, print `YES`. On the next line, print the number of shafts to seal, $c$. On each of the following $c$ lines, print the two sector IDs $u$ and $v$ of a shaft to be sealed. If multiple valid configurations exist, any one is acceptable.
If it is impossible to isolate all hubs without exceeding the power limit, print `NO`.

## Example

**Input**
```
4 3 3 5
1 2 3
1 4 2
2 4 3
3 4 4
```

**Output**
```
YES
2
1 4
2 4
```
