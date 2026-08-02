# Operational Mode Assignment

Time limit: 1 s   Memory limit: 256 MB

A facility contains $n$ components, labeled $1$ through $n$, and $m$ pairwise interference rules. Each component must be assigned to operate in either Mode 1 or Mode 2. An interference rule between two components dictates that they cannot be assigned to the same operational mode.

Determine whether a valid assignment exists. If multiple valid assignments exist, output the one that produces the lexicographically smallest sequence of modes when components are ordered from $1$ to $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interference rule between component $u$ and component $v$.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
