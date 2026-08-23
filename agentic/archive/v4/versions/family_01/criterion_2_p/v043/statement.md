# Shift Allocation

Time limit: 1 s   Memory limit: 256 MB

A facility needs to assign each of $n$ personnel members, indexed from $1$ to $n$, to one of two shifts: Shift 1 or Shift 2. The facility has $m$ incompatibility conditions, where each condition specifies two personnel members who cannot be placed on the same shift.

Determine whether there is a shift arrangement such that every member is assigned to Shift 1 or Shift 2 without violating any incompatibility conditions. If such an arrangement exists, find the one whose sequence of shift assignments $(s_1, s_2, \dots, s_n)$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that personnel member $u$ and personnel member $v$ cannot share the same shift.

## Output
If no valid shift arrangement exists, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
