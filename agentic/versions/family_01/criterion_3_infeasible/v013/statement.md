# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant operates using exactly two daily shifts. Management has compiled a list of worker pairs who cannot be assigned to the same shift due to personal disputes. 

It has already been determined that forming a valid schedule is impossible. Your task is to provide concrete evidence of this failure. 

Specifically, the given list of disputes is guaranteed to contain a group of exactly three workers who all mutually refuse to work together. That is, within this group of three, every worker has a recorded dispute with both of the other two members of the group. Since there are only two shifts available, it is strictly impossible to separate all three individuals.

You must identify a group of three workers that satisfies this condition.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of disputes, respectively. Workers are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ cannot be assigned to the same shift. Each dispute is listed at most once.

It is guaranteed that at least one group of three mutually disputing workers exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the IDs of the three workers in the group, sorted in ascending order ($a < b < c$). 

If there are multiple such groups, output the one that is lexicographically smallest. That is, minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$.

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
