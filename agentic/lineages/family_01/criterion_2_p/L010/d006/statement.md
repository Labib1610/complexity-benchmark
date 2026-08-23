# Database Schema Migration

Time limit: 1 s   Memory limit: 256 MB

A technology firm is upgrading its backend infrastructure, which consists of $n$ servers, numbered 1 through $n$. Each server must be assigned to run either Environment 1 (Legacy) or Environment 2 (Next-Gen).

The system relies on $m$ cross-validation audits. Each audit evaluates a specific pair of servers. To properly validate the data migration pipeline, every audit must compare both environments. This means for each audited pair of servers, exactly one server must be assigned to Environment 1, and the other must be assigned to Environment 2.

You need to determine if there is a valid environment assignment for all $n$ servers that satisfies the requirements of every audit.

If a valid assignment exists, the deployment tool needs to know which one to use. The tool prioritizes keeping servers on the Legacy environment (Environment 1) to minimize immediate rollout risks. Specifically, it requires the assignment sequence (consisting of 1s and 2s) that is lexicographically smallest. An assignment sequence $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first server index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of servers and the number of cross-validation audits.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of servers that must be assigned such that one runs Environment 1 and the other runs Environment 2.

## Output
If there is no way to assign environments to the servers without violating the audit constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest valid environment assignment.

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