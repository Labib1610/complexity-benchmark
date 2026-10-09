# Problem A — Independent Audits

Time limit: 2 s   Memory limit: 256 MB

You are managing the annual compliance audit for a corporation with $n$ departments. The company requires each department to be audited by exactly one of three external agencies, labeled 1, 2, and 3.

Because departments collaborate, there are $m$ joint ventures between specific pairs of departments. A joint venture is defined by an unordered pair of distinct departments.

For each joint venture between department $u$ and department $v$ (with assigned agencies $f_u$ and $f_v$), a *collaborative load* is calculated using the following formula:
$L(u,v) = (f_u - f_v)^4 - 5(f_u - f_v)^2 + 10$

The regulatory board mandates that the sum of the collaborative loads across all $m$ joint ventures must not exceed $6m$.

An assignment of agencies to all $n$ departments is legally compliant if and only if this total load condition is met.

The corporate network can be highly interconnected. You must determine whether a compliant assignment exists.

## Input
The first line provides $n$ and $m$ — the number of departments and joint ventures, respectively ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$). This bound on $m$ corresponds to at most one venture per unordered pair.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a joint venture between department $u$ and department $v$. All listed pairs are distinct up to order (so duplicates, including both $u \ v$ and $v \ u$, do not occur).

## Output
If there is no way to assign agencies to satisfy the compliance metric, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $f_1, f_2, \dots, f_n$ (where $f_i \in \{1, 2, 3\}$ is the agency for department $i$). If multiple valid assignments exist, you must provide the one that is lexicographically smallest (comparing the agency of department 1 first, then department 2, and so on).

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