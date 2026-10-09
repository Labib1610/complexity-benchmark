# Personnel Scheduling

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility maintains a roster of $n$ employees. Over time, management has recorded $m$ specific pairs of employees who exhibit detrimental friction when working together. Company policy strictly dictates that any two employees in a recorded pair cannot be assigned to the same working period. 

The facility operates continuously, utilizing exactly three distinct working periods: period 1, period 2, and period 3. 

Your task is to determine if it is possible to assign every single employee to exactly one of these three working periods such that the separation policy is never violated. If such an arrangement exists, you must also provide it.

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that employee $u$ and employee $v$ cannot share a working period.

## Output
If there is no way to assign all employees without violating the policy, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ represents the working period assigned to employee $i$. If multiple valid assignments exist, any of them will be accepted.

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
