# Problem C — Altitude Plan Rejection

Time limit: 2 s   Memory limit: 256 MB

A logistics company manages $n$ delivery drones, labeled 1 through $n$. The safety system has flagged $m$ specific pairs of drones that will cross paths during their routes. If two drones cross paths, they cannot be assigned to the same cruising altitude. It is guaranteed that the flight data contains at least one trio of drones where all three mutually cross paths—meaning every drone in the trio crosses paths with both of the other two.

The operations team initially proposed restricting the entire fleet to exactly two cruising altitudes. However, this proposal is fundamentally unworkable. Because of the existence of such a trio, no two-altitude system can possibly accommodate them without forcing two path-crossing drones to fly at the same altitude.

To finalize the rejection of the two-altitude proposal, you must provide a formal certificate of its failure. Your task is to identify one of these mutually path-crossing trios.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing that drone $u$ and drone $v$ cross paths. Each path-crossing pair is listed at most once.
It is guaranteed that at least one mutually path-crossing trio exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the labels of three drones that form a mutually path-crossing trio. The labels must be printed in ascending order ($a < b < c$).
If there are multiple such trios, you must output the one that is lexicographically smallest. That is, minimize $a$; if there is a tie, minimize $b$; and if there is still a tie, minimize $c$.

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