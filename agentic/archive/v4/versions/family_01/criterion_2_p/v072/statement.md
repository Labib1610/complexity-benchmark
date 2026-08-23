# Workforce Shift Allocation

Time limit: 1 s   Memory limit: 256 MB

An organization manages $n$ individuals, indexed from $1$ to $n$, who must each be assigned to one of two operating periods, labeled 1 and 2.

There are $m$ restriction rules provided. Each rule identifies a pair of individuals who cannot be placed in the same operating period.

Your task is to determine whether it is possible to assign every individual $i$ an operating period $s_i \in \{1, 2\}$ such that all $m$ restriction rules are satisfied. If valid assignments exist, output `YES` followed by the assignment sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest. If no assignment can satisfy every restriction, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) indicating that individual $u$ and individual $v$ cannot share the same operating period.

## Output
If no valid assignment satisfying all restrictions exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
