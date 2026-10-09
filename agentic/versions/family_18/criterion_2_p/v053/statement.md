# Chassis Configuration Search

Time limit: 5 s   Memory limit: 256 MB

## Description
A central challenge in hardware layout is finding a valid mapping of components to physical locations. You are given $n$ hardware modules that must be installed into a linear chassis featuring $n$ discrete bays, numbered $1$ through $n$. With $n!$ possible one-to-one assignments of modules to bays, the configuration space grows exceptionally fast, requiring a search of this vast permutation space to find a layout that satisfies physical constraints.

The modules are linked by $m$ point-to-point communication channels. When two linked modules are placed in bays $p$ and $q$, the channel requires a physical cable of length $|p - q|$. You are provided a maximum total cabling budget $B$, which covers the sum of the lengths of all cables. Your objective is to explore the permutation space and determine if there is any module arrangement where the sum of all $m$ cable lengths is at most $B$. There is no per-cable limit, only the overall maximum $B$.

The communication network connects all modules. Apart from a single primary module, every module is linked to exactly one supervisor module. Consequently, there are exactly $m = n-1$ channels in total.

## Input
The first line contains three integers $n$, $m$, and $B$. 
Each of the next $m$ lines contains two integers $u$ and $v$, representing a communication channel between module $u$ and module $v$. ($m = n-1$).

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ integers—the bay positions ($1$ to $n$, forming a permutation) assigned to modules $1, 2, \dots, n$ respectively—such that the total cable length is at most $B$. If no such arrangement meets the budget, print `NO`.

## Example
**Input**
```
3 2 2
1 2
1 3
```

**Output**
```
YES
2 1 3
```
