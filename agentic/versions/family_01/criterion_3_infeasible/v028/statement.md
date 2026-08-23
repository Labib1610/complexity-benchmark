# Problem C — Orbital Instability Certificate

Time limit: 2 s   
Memory limit: 256 MB

Astronomers are studying a planetary system with $n$ distinct celestial bodies, labeled 1 through $n$. Through observation, they have identified $m$ symmetric gravitational anomalies, each occurring between a specific pair of bodies.

A system is considered "critically unstable" if there exists a set of three distinct bodies where every possible pair among the three exhibits a gravitational anomaly. The presence of even one such triad is sufficient to prove that the current orbits will eventually collapse. 

You are given the catalog of anomalies for a system that is already known to be critically unstable. Your task is to isolate a specific triad of bodies that proves this instability. To ensure reproducibility in the astronomers' reports, if multiple such triads exist, you must report the one whose bodies have the smallest possible labels. Specifically, order the three bodies as $a < b < c$. Compare two candidate triads by their smallest label ($a$), breaking ties with the middle label ($b$), and finally the largest label ($c$).

The catalog is guaranteed to satisfy the following observational integrity checks:
- No body exhibits an anomaly with itself.
- No pair of bodies is listed more than once.
- The total sum of the anomaly counts across all $n$ individual bodies is exactly equal to $2m$.
- Because the system contains at least one critically unstable triad, the maximum number of anomalies associated with any single body is strictly greater than 1.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — a pair of bodies that experience a gravitational anomaly.
It is guaranteed that at least one critically unstable triad exists.

## Output
Print three integers $a$, $b$, and $c$ on one line separated by spaces, with $a < b < c$, such that all three pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) exhibit anomalies. Output the lexicographically smallest such triad.

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
