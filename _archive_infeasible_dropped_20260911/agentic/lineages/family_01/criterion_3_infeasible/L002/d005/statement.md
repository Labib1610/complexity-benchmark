# Conflict Resolution Certification

## Time and Memory Limits
Time limit: 2 s
Memory limit: 256 MB

## Description
A manufacturing facility has a roster of $n$ technicians, identified by integers from $1$ to $n$. Over time, there have been $m$ documented clashes. Each clash is an unordered pair of distinct technicians who cannot work together.

The management intended to divide the staff into two shifts, but the documented clashes make this impossible. To formally document this scheduling failure, you must locate a specific obstruction: a completely fractured triad. 

A triad is a subset of exactly three distinct technicians. A triad is considered completely fractured if all three of its 2-element subsets are present in the collection of documented clashes. 

Because the number of possible 3-element subsets is large, you must systematically search the clashes to find one. If there are multiple completely fractured triads, you must report the triad whose elements, when sorted in increasing order, form the lexicographically smallest sequence. That is, compare the smallest ID of the triads, then the middle ID, and finally the highest ID, selecting the triad with the smallest sequence of values.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), indicating the total number of technicians and the total number of clashes.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a clash between technician $u$ and technician $v$. It is guaranteed that at least one completely fractured triad exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the IDs of the three technicians in the chosen triad. If multiple such triads exist, output the one that is lexicographically smallest.

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