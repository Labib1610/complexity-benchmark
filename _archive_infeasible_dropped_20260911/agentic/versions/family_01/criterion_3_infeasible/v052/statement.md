# Problem C — Hazard Containment Failure

Time limit: 2 s
Memory limit: 256 MB

You are planning the transport of $n$ hazardous substances using exactly 2 reinforced containers. You have a manifest detailing $m$ reactive pairs of substances. If any two substances from this manifest are placed in the same container, they will cause a catastrophic reaction.

Your objective is to prove that a safe transport configuration is impossible by isolating a core group of exactly three substances, $a$, $b$, and $c$ (where $a < b < c$), that logically cannot be divided between the 2 containers without triggering a reaction. To serve as a valid proof, the chosen group must meet all of the following criteria:
- The combination of substance $a$ and substance $b$ is listed as reactive.
- The combination of substance $b$ and substance $c$ is listed as reactive.
- The combination of substance $a$ and substance $c$ is listed as reactive.

### Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a reactive pair of substances.
It is guaranteed that the provided data contains at least one group of three substances satisfying the criteria above.

### Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identified substances, ordered such that $a < b < c$. If there are multiple valid groups of three substances, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; if still tied, minimize $c$).

### Example 1
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

### Example 2
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
