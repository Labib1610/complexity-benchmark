# Problem A — Independent Audits

Time limit: 2 s   Memory limit: 256 MB

You are managing the annual compliance audit for a corporation with $n$ departments. The company requires each department to be audited by exactly one of three external agencies, labeled 1, 2, and 3.

Because departments collaborate, there are $m$ joint ventures between specific pairs of departments. The audit must be structured to meet a strict regulatory metric across these collaborations.

For every joint venture between two departments $u$ and $v$ (which are assigned agencies $f_u$ and $f_v$, respectively), an "interaction value" is computed using the following expression:
$$ 2(f_u - f_v)^4 - 10(f_u - f_v)^2 + 4 $$

An assignment of agencies to all $n$ departments is legally compliant if and only if the total sum of the interaction values over all $m$ joint ventures equals exactly $-4m$.

The corporate network can be highly interconnected, and the list of joint ventures is provided in no particular order. You must determine whether a compliant assignment exists.

## Input
The first line provides $n$ and $m$ — the number of departments and joint ventures, respectively ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a joint venture between department $u$ and department $v$. Departments are indexed from 1 to $n$.

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