# Problem C — Flight Manifest Rejection

Time limit: 2 s   Memory limit: 256 MB

A cargo company relies on two transport planes to ship various industrial chemicals. Many of these chemicals are volatile when mixed, meaning certain pairs will react dangerously and must be transported on different planes.

The current shipping manifest is fundamentally flawed: it is impossible to divide all the chemicals between just two planes without risking a reaction. Your task is to generate an automated safety rejection report. You do not need to attempt a safe allocation; you only need to prove that no such allocation exists.

To provide this proof, you must identify a set of three chemicals that inherently cannot be divided across the two planes. Specifically, you must find three chemicals such that every possible way of assigning these three to the two planes forces at least one listed reactive pair to share a plane. Because this subset cannot be safely distributed, it formally proves the overall two-plane plan is impossible.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of chemicals and the number of reactive pairs. Chemicals are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) — a pair of chemicals that react dangerously with each other. 
It is guaranteed that at least one such triplet of chemicals exists in the given data.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three chemicals that cannot be safely divided.
If there are multiple such groups, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```