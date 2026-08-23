# Operational Block Allocation

Time limit: 2 s   Memory limit: 256 MB

A research facility must organize $n$ personnel units (numbered 1 to $n$) into operational blocks. Due to interference constraints, $m$ specific pairs of personnel units are mutually incompatible and must not be assigned to the same operational block.

Exactly three distinct operational blocks are available, numbered 1, 2, and 3. Every personnel unit must be assigned to one of these three blocks.

Determine whether it is possible to assign every unit to a block such that no two incompatible units are placed in the same block. If multiple valid assignments exist, output the assignment sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest (that is, comparing $s_1$ first, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of personnel units and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u\ v$ — indicating that unit $u$ and unit $v$ are incompatible.

## Output
If no valid assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the operational block assigned to personnel unit $i$. Output the lexicographically smallest sequence among all valid assignments.

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