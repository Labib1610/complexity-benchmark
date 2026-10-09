# Committee Deadlock Resolution

## Time and Memory Limits
Time limit: 2 s
Memory limit: 256 MB

## Description
A selection panel is evaluating a roster of candidates, numbered $1$ to $n$. During the vetting process, the panel recorded mutual vetoes. Each veto is an unordered pair of distinct candidates who cannot be placed on the same committee.

For each candidate, we define their *incompatibility domain* as a set containing the candidate themselves, plus every other candidate with whom they share a recorded mutual veto.

To formally document a scheduling failure, you must locate a specific obstruction: a deadlocked trio. A trio is defined as a set of exactly three distinct candidates. A trio is considered deadlocked if the trio is a subset of the incompatibility domain of each of its three members.

You must systematically evaluate the vetoes to find a deadlocked trio. If there are multiple deadlocked trios, you must report the trio whose candidate numbers form the lexicographically smallest sequence when sorted in ascending order. (A sequence $a_1 < b_1 < c_1$ is lexicographically smaller than $a_2 < b_2 < c_2$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$ and $b_1 = b_2$ and $c_1 < c_2$).

## Input
The first line contains two integers $n$ and $m$, indicating the candidate headcount and the log size. The headcount $n$ starts from a minimum of 3 and reaches up to the interview limit of 2000. The log size $m$ is at least 3 and is bounded by the database capacity of 200,000 entries, or the maximum possible number of unique pairs for $n$ candidates, whichever is more restrictive.
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