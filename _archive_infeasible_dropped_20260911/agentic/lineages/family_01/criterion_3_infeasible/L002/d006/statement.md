# Committee Deadlock Resolution

## Time and Memory Limits
Time limit: 2 s
Memory limit: 256 MB

## Description
A selection panel is evaluating $n$ candidates, numbered $1$ to $n$. During the vetting process, the panel recorded $m$ mutual vetoes. Each veto is an unordered pair of distinct candidates who cannot be placed on the same committee.

To formally document a scheduling failure, you must locate a specific obstruction: a deadlocked trio. 

For any two distinct candidates $x$ and $y$, define the indicator value $V(x, y) = 1$ if the unordered pair of $x$ and $y$ is present in the recorded list of mutual vetoes, and $V(x, y) = 0$ otherwise. A trio is a set of exactly three distinct candidates $\{x, y, z\}$. A trio is considered deadlocked if the sum of the indicators for its pairs is exactly 3; that is, $V(x, y) + V(y, z) + V(x, z) = 3$.

You must systematically evaluate the vetoes to find a deadlocked trio. If there are multiple deadlocked trios, you must report the trio whose candidate numbers form the lexicographically smallest sequence when sorted in ascending order. (A sequence $a_1 < b_1 < c_1$ is lexicographically smaller than $a_2 < b_2 < c_2$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$ and $b_1 = b_2$ and $c_1 < c_2$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), indicating the total number of candidates and the total number of recorded vetoes.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a mutual veto between candidate $u$ and candidate $v$. It is guaranteed that at least one deadlocked trio exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the candidate numbers in the chosen trio. Among all valid deadlocked trios, output the lexicographically smallest one (smallest $a$; if tied, smallest $b$; if tied, smallest $c$).

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