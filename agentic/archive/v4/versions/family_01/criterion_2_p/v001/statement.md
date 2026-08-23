# Problem B — Team Allocation

Time limit: 1 s   Memory limit: 256 MB

An organization needs to partition $n$ members, indexed from $1$ to $n$, into two distinct teams labeled 1 and 2. There are $m$ pair restrictions: each restriction specifies two members who cannot be assigned to the same team.

Determine whether it is possible to assign every member to team 1 or team 2 such that no restriction is violated. If multiple valid assignments exist, output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that member $u$ and member $v$ cannot share the same team.

## Output
If no valid team assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
