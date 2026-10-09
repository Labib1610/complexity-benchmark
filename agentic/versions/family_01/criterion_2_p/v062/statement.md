# Problem B — Phase Scheduling

Time limit: 1 s
Memory limit: 256 MB

A manufacturing facility requires a daily operational configuration vector $S = (s_1, s_2, \dots, s_n)$. Each parameter $s_i$ corresponds to a technician and must be assigned a phase, chosen from the domain $\{1, 2\}$. 

To prevent operational failures, you must evaluate the configuration space of size $2^n$ to find a valid assignment. The restrictions are given as $m$ interference rules. Each rule specifies two technicians, $u$ and $v$, who share specialized tools. A configuration is strictly invalid if it assigns $s_u = s_v$ for any of these given pairs.

You must search for the lexicographically first sequence $S$ that satisfies all $m$ restrictions. If the entire space of $2^n$ configurations contains no valid assignment, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of technicians governed by an interference rule.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest valid configuration.

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
