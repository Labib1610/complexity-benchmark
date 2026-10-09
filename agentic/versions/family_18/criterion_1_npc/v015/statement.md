# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A control vault requires $n$ control units to be installed into a backbone trench containing exactly $n$ consecutive installation bays. Each unit must be assigned to exactly one bay.

The design specifies $m$ point-to-point communication links that must be routed between specific pairs of units. The trench's straight layout means the physical length of each link is exactly the absolute difference between the bay numbers of the two units it connects.

Procurement has supplied a total wiring budget of $B$ length units. Because multiple links can share the trench's wiring conduit without interference, the only restriction is that the sum of the lengths of all $m$ links must not exceed $B$.

Determine if a valid placement of units exists within this budget.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a communication link is required between unit $u$ and unit $v$.

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the bay number (from $1$ to $n$) assigned to unit $1, 2, \dots, n$ respectively.
If no such placement exists, print `NO`.

## Example 1
### Input
```
3 2 2
1 2
2 3
```
### Output
```
YES
1 2 3
```

## Example 2
### Input
```
3 3 3
1 2
2 3
3 1
```
### Output
```
NO
```
