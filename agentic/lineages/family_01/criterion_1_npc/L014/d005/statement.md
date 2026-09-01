# Problem A — Independent Audits

Time limit: 2 s   Memory limit: 256 MB

You are coordinating the annual compliance review for $n$ corporate departments. Each department must be assigned to exactly one of three external auditing firms, which are identified by the integers 1, 2, and 3.

To prevent conflicts of interest, the review must account for internal dependencies. There are $m$ known joint ventures, each involving a specific pair of departments. 

Each auditing firm is associated with a specific 4-dimensional compliance signature vector:
- Firm 1 uses signature $V_1 = (1, 1, 1, 1)$
- Firm 2 uses signature $V_2 = (1, -1, 1, -1)$
- Firm 3 uses signature $V_3 = (1, 1, -1, -1)$

When two departments $u$ and $v$ are involved in a joint venture, their "venture score" is calculated as the standard dot product of the signature vectors of their assigned firms, $V_{f_u} \cdot V_{f_v}$. 

The entire corporate assignment is considered 'compliant' if and only if the total sum of the venture scores across all $m$ joint ventures is exactly 0. 

Be aware that the test suite contains arbitrary, dense compliance networks, and the joint ventures may be presented in an adversarial sequence.

Determine if there is a valid firm assignment for all $n$ departments that perfectly satisfies this compliance rule.

## Input
The first line contains two integers $n$ and $m$ — the number of departments and the number of joint ventures ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of departments involved in a joint venture. Departments are numbered 1 through $n$.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $f_1, f_2, \dots, f_n$ (each in $\{1, 2, 3\}$), where $f_i$ is the auditing firm assigned to department $i$. Among all valid assignments, output the one that is lexicographically smallest (compare $f_1$ first, then $f_2$, and so on).

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