# Problem A — Museum Curation

Time limit: 2 s   Memory limit: 256 MB

You are organizing a highly anticipated exhibition featuring $n$ interactive installations. The venue supports exactly three distinct frequency multipliers for the installations' audio elements, designated as 1, 2, and 3.

Every installation $i$ must be assigned exactly one frequency multiplier $c_i \in \{1, 2, 3\}$. However, certain pairs of installations interact. You have compiled a list of $m$ interacting pairs. For any such pair $(u, v)$, their combined acoustic profile is evaluated by taking the product of their assigned frequency multipliers. 

To ensure no acoustic interference occurs, this product must never be a perfect square. If the product of the two multipliers is a perfect square, it creates an unstable resonance loop and the assignment is invalid.

You must determine whether it is possible to assign a frequency multiplier to all $n$ installations such that this interference condition is strictly avoided for all given pairs.

## Input
The first line contains two integers $n$ and $m$ — the number of installations and the number of interacting pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing an interacting pair of installations. Installations are indexed from 1 to $n$.

## Output
If no such assignment is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the frequency multiplier assigned to installation $i$. If multiple valid assignments exist, you may output any of them.

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