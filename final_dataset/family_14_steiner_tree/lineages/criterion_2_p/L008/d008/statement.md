# Resonance Containment

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of $R$ distinct resonant entities. These entities interact through $S$ bidirectional harmonic links. The system is minimally cohesive: every entity can influence every other entity through a sequence of links, but the removal of any single link would shatter this property. 

A recent protocol requires that a specific set of $P$ entities must be fully activated. You may additionally activate any other entities you choose. 

To ensure stability, the complete set of activated entities must be *synchronous*. A set of activated entities is synchronous if it is impossible to partition it into two non-empty subsets such that no harmonic link exists between an entity in the first subset and an entity in the second subset. 

Activating entities has a cost. Specifically, each harmonic link has a characteristic penalty $w$. If both entities associated with a link are activated, the link becomes "saturated" and adds its penalty $w$ to the total system cost. If one or neither of the associated entities is activated, the link remains dormant and contributes 0 to the total cost.

Your objective is to determine the minimum possible total penalty of the saturated links such that all $P$ mandated entities are activated and the entire set of activated entities is synchronous.

## Input

The first line contains three integers $R$, $S$, and $P$. 
The total number of entities $R$ satisfies $1 \le R \le 200000$. 
Because the system is minimally cohesive, the number of harmonic links $S$ is exactly equal to $R - 1$. 
The number of mandated entities $P$ satisfies $1 \le P \le R$.

The second line contains $P$ distinct integers representing the identifiers of the mandated entities.

Each of the following $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$). This indicates a harmonic link between entity $u$ and entity $v$ with a characteristic penalty of $w$ ($1 \le w \le 1000000$). 

## Output

Output a single integer representing the minimum possible total penalty of the saturated links under the given conditions.

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