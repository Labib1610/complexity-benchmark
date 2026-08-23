# Problem B — Kinetic Dampening System

Time limit: 1 s   Memory limit: 256 MB

A heavy industrial facility utilizes $n$ oscillating dampeners, numbered 1 to $n$. To calibrate the system, each dampener must be configured with an amplitude setting of either 1 or 2.

The facility contains $m$ structural linkages, each connecting a specific pair of dampeners. The stress on a linkage is determined by the kinetic energy of the connected dampeners, which scales with the square of their amplitude settings. To prevent structural failure, the absolute difference between the squares of the amplitude settings of any two connected dampeners must be exactly 3.

You must determine if there is a valid configuration of amplitude settings for all $n$ dampeners that ensures the stability of all $m$ linkages. If a valid configuration exists, you must output it. In cases where multiple valid configurations satisfy all requirements, you must output the configuration that forms the lexicographically smallest sequence of amplitude settings.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the numbers of two dampeners connected by a linkage.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of amplitude settings.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```