# Optimal Slot Assignment for Signal Relays

Time limit: 5 s
Memory limit: 256 MB

## Description
A facility has $n$ relay units that must be installed into a single row of $n$ mounting slots. You must assign each unit to exactly one distinct slot position, numbered 1 through $n$. There are $n!$ possible permutations for this assignment, and you must evaluate this space of configurations to find one that satisfies a total budget constraint.

The units must be wired together according to a given schematic specifying $m$ bidirectional signal links between specific pairs of units. Any two units can communicate through exactly one valid sequence of links. For any given assignment, the length of the cable required for a link between a unit in slot $x$ and a unit in slot $y$ is $|x - y|$. The total cabling cost of an assignment is the sum of these lengths over all $m$ links.

You have a total cabling budget of $B$. You must search for a one-to-one placement of the units onto the line of slots whose total cabling cost is at most $B$, or report that no such placement exists.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a signal link between unit $u$ and unit $v$.

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ integers representing the assigned slot positions (from $1$ to $n$) for units $1, 2, \dots, n$ respectively. If there are multiple valid placements, any one is acceptable.
If no placement can meet the budget, print `NO`.

## Example 1

**Input:**
```
5 4 6
1 2
1 3
1 4
1 5
```

**Output:**
```
YES
3 1 2 4 5
```

## Example 2

**Input:**
```
5 4 5
1 2
1 3
1 4
1 5
```

**Output:**
```
NO
```
