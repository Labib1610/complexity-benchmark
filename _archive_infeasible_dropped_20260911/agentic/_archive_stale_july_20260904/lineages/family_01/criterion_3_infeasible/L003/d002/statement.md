# Problem C — Roster Evaluation

Time limit: 2 s   Memory limit: 256 MB

Factory management is reviewing historical worker rosters to pinpoint the source of a specific scheduling dysfunction. You are given a log of past disputes, where each entry records a conflict between a pair of workers. Your objective is to analyze this log and identify a three-person deadlock. A deadlock of this type consists of exactly three distinct workers who all mutually conflict—meaning each worker in the trio has a recorded dispute with the other two members of the trio.

Because these logs were taken from a period where the factory was unable to form two conflict-free shifts, the records are certain to contain at least one such three-person deadlock. Your task is to extract one of these groups.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), denoting the total number of workers and the total number of recorded disputes.
Following this, there are $m$ lines. Each line contains two integers $u$ and $v$, representing a dispute between worker $u$ and worker $v$.
The provided data inherently contains at least one three-person deadlock.

## Output
Output a single line containing three space-separated integers $a$, $b$, and $c$, ordered such that $a < b < c$. These integers must represent the workers forming a three-person deadlock. Should there be more than one such group, you must output the sequence that comes first lexicographically (minimizing $a$; then minimizing $b$ in the event of a tie; and finally minimizing $c$).

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