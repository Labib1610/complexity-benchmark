# Orbital Station Life-Support

Time limit: 2 s   Memory limit: 256 MB

An orbital station consists of $n$ habitat modules, numbered 1 through $n$. To ensure redundancy, the station provides exactly three independent life-support grids, designated as grid 1, grid 2, and grid 3. Each module must be connected to exactly one of these three grids.

Certain pairs of modules share a direct ventilation corridor. If two modules sharing a corridor are connected to the same life-support grid, a pressure differential error will trigger a station-wide alarm. You are provided with a complete list of $m$ such corridors. The safety constraint is strictly local: for any corridor connecting module $u$ and module $v$, if $u$ is on grid $k$, then $v$ must be on a grid other than $k$. 

In many cases, a module's assignment can be deduced directly from its surroundings. For example, if a module's neighbors operate on grid 1 and grid 2, the local exclusion principle forces the module to be assigned to grid 3. 

Your task is to find a valid grid assignment for all $n$ modules. Because grid 1 is the most energy-efficient, followed by grid 2, and then grid 3, the station's automated system prioritizes lower-numbered grids. Specifically, the system evaluates the modules sequentially from 1 to $n$, always preferring the lowest possible grid number for the current module. Therefore, if multiple valid assignments exist, you must output the one that is lexicographically smallest (i.e., minimize the grid number for module 1; in the event of a tie, minimize the grid number for module 2, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of modules and the number of ventilation corridors.
The next $m$ lines each contain two integers $u$ and $v$, indicating that module $u$ and module $v$ share a corridor.

## Output
If no valid grid assignment exists that satisfies all local exclusion constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $g_1, g_2, \dots, g_n$ (where each $g_i \in \{1, 2, 3\}$), representing the grid assigned to each module. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
