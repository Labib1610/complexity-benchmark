# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still operates using only two shifts. However, management has realized that the current personnel roster cannot possibly be divided into just two shifts without violating constraints. Your task is not to attempt an allocation, but to document exactly why it fails.

Certain pairs of workers are incompatible and cannot be assigned to the same shift. It is guaranteed that the incompatibility records contain at least one group of three workers where every individual in the group is incompatible with the other two. Any such trio provides indisputable evidence that two shifts are insufficient. You must identify one such trio.

## Input
The first line contains two integers $n$ and $m$. The integer $n$ represents the number of workers (numbered $1$ to $n$), and $m$ represents the number of incompatibility records.
To ensure the administrative systems can handle the records, the quantity $n(n-1)$ is guaranteed to be between $6$ and $3,998,000$ inclusive.
The number of records $m$ is at least $3$, cannot exceed the total number of possible distinct pairs of workers, and satisfies the condition that $5m \le 1,000,000$.

Each of the next $m$ lines contains two integers $u$ and $v$ — representing an incompatible pair of workers.
It is guaranteed that at least one trio of mutually incompatible workers exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, separated by spaces, representing the IDs of three mutually incompatible workers.
The three IDs must be printed in ascending order ($a < b < c$).
If there are multiple such trios, you must output the one that is lexicographically first (i.e., the trio with the smallest $a$; in case of a tie, the one with the smallest $b$; and if still tied, the one with the smallest $c$).

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
