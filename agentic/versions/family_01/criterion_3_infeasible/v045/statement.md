# Problem C — Calibration Triplet

Time limit: 2 s   Memory limit: 256 MB

You are configuring a network of $n$ communication relays. Certain pairs of relays share a vulnerable frequency band, which causes mutual interference when both are active. 

To run a stress test on the network's error-correction protocols, you need to isolate a specific configuration: a set of exactly three distinct relays such that mutual interference occurs between all pairs formed from these three relays. 

## Input
The first line contains two integers $n$ and $m$ (3 ≤ $n$ ≤ 2000, 3 ≤ $m$ ≤ min($n$·($n$−1)/2, 2·10⁵)), where $n$ is the number of relays and $m$ is the number of interfering pairs.
The relays are numbered from 1 to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that relay $u$ and relay $v$ interfere with each other.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the chosen relays. 
The three integers must be printed in ascending order ($a < b < c$). 
If multiple sets of three relays meet the criteria, output the one that is lexicographically first (i.e., the one with the smallest value of $a$; in case of a tie, the one with the smallest value of $b$; and if still tied, the smallest value of $c$).

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
