# Problem B — Dual-Mode Operation

Time limit: 1 s   Memory limit: 256 MB

A system consists of $n$ modules, numbered 1 to $n$. The system operates using two distinct operational modes, labeled 1 and 2.
There are $m$ interference links, each connecting a pair of modules. If two modules connected by an interference link are set to the same operational mode, a critical failure occurs.

You must assign exactly one mode to each module such that no critical failure can occur. Due to power constraints, your assignment must also satisfy a load-balancing condition: the absolute difference between the number of modules assigned to mode 1 and the number of modules assigned to mode 2 must not exceed $n$. 

Furthermore, the system architecture guarantees that no single module appears as an endpoint in more than $m$ interference links.

If there is no way to assign the modes while avoiding critical failures, report impossibility. Otherwise, output the valid assignment. If multiple valid assignments exist, you must output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of modules connected by an interference link.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
