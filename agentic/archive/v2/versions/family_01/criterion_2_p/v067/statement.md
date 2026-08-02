# Factory Roster Scheduling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates under two distinct configuration modes, labeled Mode 1 and Mode 2. The plant employs $n$ personnel, indexed from $1$ to $n$. Due to shared resource limitations, certain pairs of personnel cannot be assigned to the same configuration mode simultaneously. You are given $m$ pairwise exclusion rules, where each rule specifies two personnel who must receive different modes.

To maintain operational compliance, any valid assignment $(s_1, s_2, \dots, s_n)$ with $s_i \in \{1, 2\}$ must satisfy all $m$ exclusion rules. Additionally, the facility mandates the following operational guidelines:
1. **Isolated Personnel Rule**: Any staff member who is not involved in any exclusion rule must be assigned to Mode 1.
2. **Priority Score Minimization**: Among all valid mode assignments that satisfy the exclusion rules and the Isolated Personnel Rule, you must select the configuration that minimizes the overall facility priority score $S$, defined as:
$$S = \sum_{i=1}^{n} s_i \cdot 3^{n-i}$$

Determine whether a valid mode assignment exists. If so, output `YES` followed by the sequence of assigned modes that minimizes $S$. Otherwise, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of mutual exclusion constraints, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that person $u$ and person $v$ cannot share the same operational mode.

## Output
If no valid assignment satisfies all constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the assignment that minimizes the priority score $S$.

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
