# Problem B — Factory Roster Separation

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates across two distinct work slots, numbered 1 and 2. The workforce consists of $n$ personnel, identified by unique IDs from $1$ to $n$. Certain pairs of personnel are mutually incompatible and cannot be assigned to the same work slot.

Your task is to assign each person to exactly one work slot (1 or 2) such that no incompatible pair operates in the same slot. If several valid slot assignments exist, you must select the one that forms the lexicographically smallest sequence of slot numbers $s_1, s_2, \ldots, s_n$. If no valid arrangement is possible, report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$, representing the total number of personnel and the total number of incompatibility restrictions, respectively ($1 \le n \le 200\,000$, $0 \le m \le 200\,000$).

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that person $u$ and person $v$ cannot share a work slot.

## Output
If no valid slot assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid slot assignment.

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
