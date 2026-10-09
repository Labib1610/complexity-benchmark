# Deadlock Certification

Time limit: 2 s
Memory limit: 256 MB

The factory employs $n$ workers. Over time, $m$ mutual grievances have been filed between pairs of workers, meaning those two individuals refuse to work together. The administration needs to divide the workforce into two shifts, but the situation has deteriorated to the point where a valid assignment is impossible.

Your task is to certify this impossibility by identifying a subset of workers that is completely deadlocked. A subset is completely deadlocked if every single pair of workers within it has a mutual grievance. Evaluating the stability of all possible subsets to find a deadlock is an enormous task, as the space of possible combinations explodes in size with the number of workers. Searching through all subsets of arbitrary sizes to find one where every member refuses to work with every other member is computationally daunting.

For the official certification, however, you are required to submit a deadlocked subset containing exactly three workers. You are guaranteed that at least one such subset exists in the grievance logs. Output the three worker IDs in increasing order. To ensure uniformity in reporting, if there are multiple qualifying subsets, you must output the one that is lexicographically first (i.e., the smallest first ID; in case of a tie, the smallest second ID; and finally the smallest third ID).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of mutual grievances.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — a pair of workers who have a mutual grievance. Each grievance is listed at most once.
It is guaranteed that at least one deadlocked subset of exactly three workers exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that all three pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) have mutual grievances. Output the lexicographically smallest such triplet.

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
