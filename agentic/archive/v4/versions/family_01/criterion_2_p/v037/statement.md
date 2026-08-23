# Shift Allocation

Time limit: 1 s   Memory limit: 256 MB

A facility operates two shifts, labeled 1 and 2. Given $n$ personnel and $m$ incompatibility pairs, assign each person a shift so that no incompatible pair shares a shift, or report that no such assignment exists. If multiple valid shift schedules exist, determine the lexicographically smallest sequence of shift assignments.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ ranges from a single person up to the facility's total worker capacity of two hundred thousand ($1 \le n \le 2 \cdot 10^5$). The number of conflict pairs $m$ is non-negative and bounded by that same upper limit ($0 \le m \le 2 \cdot 10^5$).

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), denoting a pair of mutually incompatible workers.

## Output
If no valid assignment exists, print a single line `NO`.

Otherwise, print `YES`, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
