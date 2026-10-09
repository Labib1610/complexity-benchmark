# Problem B — Backplane Module Placement

Time limit: 5 s   Memory limit: 256 MB

## Description
A hardware assembly consists of $n$ modules that must be inserted into $n$ evenly spaced slots along a straight rail. The slots are numbered sequentially from $1$ to $n$. Each module must be placed into exactly one slot, requiring a one-to-one mapping of modules to slot numbers.

The modules must communicate via a set of $m$ point-to-point data cables. The cabling architecture is designed so that a signal can travel between any two modules across some sequence of cables. To avoid redundancy, the network is built with exactly $m = n-1$ cables to achieve this full interconnectivity.

The amount of cable required to connect two modules is determined by the physical distance between them on the rail, which is exactly the absolute difference between their assigned slot numbers. The direction of the connection and the physical connectors do not add to this length. The assembly has a maximum total cable allowance, $B$, which applies to the sum of the lengths of all cables used. There is no limit on individual cable lengths or on the number of cables passing through any section of the rail.

Determine if there is a valid assignment of the $n$ modules to the $n$ slots such that the sum of all cable lengths does not exceed $B$. If possible, provide one such assignment.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing a cable between module $u$ and module $v$. (It is guaranteed that $m = n-1$ and full interconnectivity is maintained).

## Output
If the budget can be met, print `YES` on the first line. On the second line, print $n$ integers representing the slot numbers (from $1$ to $n$) assigned to module 1, module 2, ..., module $n$. If the budget cannot be met, print `NO`.

## Example

### Input
```text
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```text
YES
4 5 3 1 2
```
