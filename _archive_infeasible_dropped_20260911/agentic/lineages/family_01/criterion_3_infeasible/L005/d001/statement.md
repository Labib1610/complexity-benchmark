# Problem C — Justifying the Roster Failure

Time limit: 2 s
Memory limit: 256 MB

The management wants to assign all personnel to two distinct working periods. They have collected a list of preliminary friction reports, each indicating that two specific individuals should ideally not share a working period. 

However, management will only formally declare the two-period assignment impossible if they can identify a *corroborated conflict*. A preliminary report between individual $u$ and individual $v$ is classified as a corroborated conflict if and only if there exists a third individual $w$ who also has a preliminary report with $u$ and a preliminary report with $v$. 

When such a situation occurs, the group of three individuals (the two from the initial report, plus their corroborator $w$) forms a logical contradiction, making it strictly unachievable to divide them into just two periods without someone sharing a period with someone they have a report against.

The management guarantees that the provided records contain at least one such group of three individuals. Your task is to identify one such group to justify the roster failure.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of personnel and the number of preliminary reports, respectively. Personnel are numbered from 1 to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a preliminary report involving individual $u$ and individual $v$. All reports are distinct (no pair of individuals is listed more than once).

It is guaranteed that at least one corroborated conflict (and thus its associated group of three individuals) exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, satisfying $a < b < c$, representing the three individuals involved in the corroborated conflict.

If there are multiple such groups, output the one that comes first lexicographically (minimize $a$; in case of a tie, minimize $b$; and finally minimize $c$).

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