# Problem C — Roster Evaluation

Time limit: 2 s   Memory limit: 256 MB

The factory management is analyzing the worker roster to identify a specific dysfunction pattern. You are provided with a list of recorded disputes between pairs of workers. Your task is to process this roster and locate a three-person deadlock. A three-person deadlock is a group of exactly three workers where every single worker in the group has a recorded dispute with both of the other workers in that same group. 

It is guaranteed that the records contain at least one such group. Your job is to output one of these groups.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of recorded disputes, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a dispute between worker $u$ and worker $v$.
It is guaranteed that at least one three-person deadlock exists in the given data.

## Output
Print three integers $a$, $b$, and $c$, separated by spaces, on a single line such that $a < b < c$. These three workers must form a three-person deadlock. If multiple valid groups exist, output the lexicographically smallest sequence (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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