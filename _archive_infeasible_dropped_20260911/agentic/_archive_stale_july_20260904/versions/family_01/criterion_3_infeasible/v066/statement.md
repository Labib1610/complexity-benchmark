# Problem C — Structural Incompatibility

Time limit: 2 s
Memory limit: 256 MB

The scheduling system attempts to assign all active operations into exactly two available processing windows. However, the current configuration of operations is known to be fundamentally incompatible with a two-window schedule. Your objective is not to find a valid arrangement, but to provide concrete evidence of this incompatibility.

You are given a log of conflicting pairs of operations. A conflict means the two operations cannot safely share the same processing window. It is guaranteed that the log contains at least one cluster of three mutually conflicting operations (where each operation in the trio conflicts with both of the others). Any such cluster logically proves that two processing windows are insufficient. You must identify and output one such cluster.

## Input
The first line provides two integers, $n$ and $m$. The integer $n$ represents the number of active operations. It is bounded below by the minimum number of operations required to form a conflicting trio, and bounded above by the facility's hardware ceiling of exactly two thousand concurrent operations. The integer $m$ represents the total number of recorded conflict pairs. It is bounded below by the exact number of conflicts present in a single isolated trio. It will not exceed the theoretical maximum number of unique pairs that can be formed from the $n$ operations, nor will it surpass the database's strict limit of two hundred thousand records.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that operation $u$ and operation $v$ conflict. Operations are numbered starting from 1. It is guaranteed that at least one cluster of three mutually conflicting operations exists within this data.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, satisfying $a < b < c$. These must represent three operations where the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all listed as conflicts. If multiple such clusters exist, you must output the one that is lexicographically smallest (the one with the smallest value for $a$; in case of a tie, the smallest value for $b$; and if still tied, the smallest value for $c$).

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
