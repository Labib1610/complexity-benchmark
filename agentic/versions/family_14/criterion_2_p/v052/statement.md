# Phase 2: High-Priority Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

A cybersecurity firm is executing a hardware upgrade project at a large facility. The project is managed in three phases.

**Phase 1: Facility Survey.** Engineers map the existing conduit infrastructure between $n$ equipment rooms (numbered 1 to $n$). The facility's architectural records show that the conduit network was built incrementally in the past. Starting with $n$ entirely isolated rooms, builders installed exactly $m$ conduit segments. Every time a segment was added, it was strictly chosen to link two rooms that previously had no way to route data to each other, directly or indirectly. By the end of this process, a unified network was formed where data could flow between any given pair of rooms. 

**Phase 2: Cable Planning.** You are responsible for this phase. The client has identified $t$ key rooms that require high-bandwidth connectivity. Your task is to select a subset of the surveyed conduit segments to receive new fiber optic cables. The selected segments must form a network that allows all $t$ key rooms to communicate with one another (data can pass through non-key intermediate rooms if necessary). Given the installation cost for each conduit segment, you must determine the absolute minimum total cost to achieve this requirement.

**Phase 3: Procurement.** The finance team takes the minimum cost from Phase 2, applies a 20% contingency markup, and finalizes the budget.

Write a program to execute Phase 2. Given the surveyed segments from Phase 1 and the list of key rooms, output the exact minimum installation cost before any Phase 3 markups are applied.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers representing the identifiers of the key rooms.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a surveyed conduit segment connecting room $u$ and room $v$ with an installation cost of $w$. 
The provided segments are guaranteed to reflect the completed network from the incremental build process described in Phase 1.

## Output

Print a single integer: the minimum total cost calculated in Phase 2.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
