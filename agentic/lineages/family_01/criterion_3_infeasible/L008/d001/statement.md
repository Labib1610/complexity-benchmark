# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

Management is attempting to divide the factory workforce into exactly two shifts, but the proposed constraints make this impossible. Your task is to provide concrete evidence of this impossibility rather than attempting to build a schedule. 

You are given a log of conflict records; each record indicates a specific pair of workers who refuse to be assigned to the same shift. The logs guarantee the existence of at least one triplet of workers where all three individuals have mutual conflicts with each other. Identifying any such triplet conclusively demonstrates that two shifts are inadequate. You must find and output one such triplet.

## Input
The first line provides two integers, $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of conflict records, respectively. Workers are identified by integers from $1$ to $n$.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), representing a conflict between worker $u$ and worker $v$.
It is guaranteed that the provided records contain at least one triplet of mutually conflicting workers.

## Output
Output three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing a triplet of workers where the conflicts $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the input. If there is more than one such triplet, you must output the one that minimizes the conflict score, defined as $a \cdot 10^8 + b \cdot 10^4 + c$.

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