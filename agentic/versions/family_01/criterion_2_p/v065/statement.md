# Factory Roster Optimization

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates under two distinct operational modes, designated as Mode 1 and Mode 2. The plant employs $n$ personnel, numbered $1$ through $n$. There are $m$ restriction rules given between pairs of personnel. Each rule specifies two personnel who cannot be assigned to the same operational mode.

We say two personnel belong to the same restriction group if they are directly linked by a restriction rule, or indirectly linked through a sequence of restriction rules. To comply with plant protocol, the final mode assignment must satisfy the following requirement:
- Within each restriction group, the person with the smallest numeric identifier among all members of that group must be assigned to Mode 1.

Your task is to determine whether it is possible to assign every person to either Mode 1 or Mode 2 such that no restriction rule is violated and the plant protocol is met. If valid assignments exist, output the mode sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of restriction rules, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that person $u$ and person $v$ cannot share the same operational mode.

## Output
If no valid assignment satisfies all constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid mode assignment.

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
