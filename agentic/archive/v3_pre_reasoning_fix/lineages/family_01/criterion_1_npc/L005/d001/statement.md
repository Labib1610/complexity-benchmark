# Problem A — Platform Drainage

Time limit: 2 s   Memory limit: 256 MB

You are designing a multi-level architectural installation. The structure is supported by $n$ vertical pillars, numbered 1 through $n$. For aesthetic and structural reasons, each pillar must be built to a height of exactly 1, 2, or 3 meters.

The installation includes $m$ straight walkways. Each walkway spans exactly between two specific pillars. To ensure proper water drainage during rainstorms, no walkway is allowed to be perfectly level. Consequently, any two pillars connected by a walkway must be constructed to strictly different heights.

Your task is to determine a valid height for each of the $n$ pillars. Since many valid height configurations might exist, the construction team requires a deterministic blueprint. You must provide the configuration that is lexicographically first. That is, you must choose a valid configuration that minimizes the height of pillar 1; in the event of ties, it must minimize the height of pillar 2, and so forth.

If it is impossible to assign heights of 1, 2, or 3 meters to all pillars such that every walkway is sloped, the design is unbuildable.

## Input
The first line of the input contains two integers $n$ and $m$ — the number of pillars and the number of walkways (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n \cdot (n-1)/2$). 
Each of the following $m$ lines contains two integers $u$ and $v$ — indicating that a walkway connects pillar $u$ and pillar $v$.

## Output
If the design is unbuildable because no valid height assignment exists, print a single line containing `NO`. 
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $h_1, h_2, \dots, h_n$ (each in $\{1, 2, 3\}$), where $h_i$ is the height of pillar $i$ in meters. Remember to output the lexicographically smallest valid sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```