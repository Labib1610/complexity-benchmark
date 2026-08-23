# Chamber Pressure Assignment

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ storage chambers, indexed $1$ through $n$. Each chamber must be assigned a pressure level chosen from the set $\{1, 2, 3\}$.

There are $m$ structural interactions between pairs of chambers. Each interaction links a pair of distinct chambers $(u, v)$ and requires that they do not operate at the same pressure level. That is, if a pair $(u, v)$ is specified, the assigned pressure levels $s_u$ and $s_v$ must satisfy $s_u \neq s_v$.

Find an assignment of pressure levels $s_1, s_2, \dots, s_n \in \{1, 2, 3\}$ for all chambers such that $s_u \neq s_v$ for every specified interaction pair $(u, v)$. If multiple valid assignments exist, output the one that produces the lexicographically smallest tuple $(s_1, s_2, \dots, s_n)$. If no valid assignment exists, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of chambers and the number of structural interaction pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that chamber $u$ and chamber $v$ cannot share the same pressure level.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2, 3\}$ is the pressure level assigned to chamber $i$, choosing the lexicographically smallest sequence among all valid assignments.

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