# Problem C — Mechanical Jam

Time limit: 2 s   Memory limit: 256 MB

You are inspecting the schematics for a prototype gearbox containing $n$ cogwheels. The schematic lists $m$ contact points where a specific pair of cogwheels interlock.

In a functioning gear train, any interlocking cogwheels must rotate in opposite directions. However, this prototype is inherently flawed and cannot turn. Your objective is to isolate the source of the jam. Specifically, the schematic is guaranteed to contain at least one set of three cogwheels that are all mutually interlocked (each of the three connects directly to the other two). Such a configuration creates a mechanical paradox, halting the entire system. You must identify one of these locked sets.

## Input
The first line provides $n$ and $m$ (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of cogwheels and interlocking pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$, indicating that cogwheel $u$ and cogwheel $v$ are interlocked.
The input will always contain at least one mutually interlocking set of three cogwheels.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These must represent a set where the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the input. If there are multiple such sets, provide the one that is lexicographically first (prioritizing the lowest value for $a$, then the lowest for $b$, and finally $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```