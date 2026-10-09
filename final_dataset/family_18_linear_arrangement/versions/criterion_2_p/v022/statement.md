# Optimal Component Alignment in 1D Space

Time limit: 5 s
Memory limit: 256 MB

## Description
You are tasked with mapping a set of $n$ entities to $n$ distinct integer coordinates in the range $[1, n]$. You are also given a list of $m$ pairwise interactions between these entities. The cost of a mapping is the sum of the absolute differences in coordinates for all interacting pairs. 

Because there are $n!$ valid ways to arrange the entities, the configuration space is vast. You are provided with a target threshold $B$. Your goal is to find a mapping of entities to coordinates such that the total cost for all specified interactions is less than or equal to $B$.

The interactions in this instance form a globally integrated system: it is possible to transition between any two entities via a sequence of interactions. Furthermore, the system is strictly minimal to prevent redundant dependencies, meaning there are exactly $m = n - 1$ interactions in total. 

Determine if a valid mapping exists within the $n!$ permutations that satisfies the budget $B$, and if so, provide one such mapping.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing an interaction between entity $u$ and entity $v$ (entities are 1-indexed).

## Output
If a valid mapping exists, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the assigned coordinate (from $1$ to $n$) for entity $1, 2, \dots, n$ respectively. 
If no such mapping exists, print `NO`.

## Example

**Input:**
```
4 3 4
1 2
2 3
2 4
```

**Output:**
```
YES
1 2 3 4
```
