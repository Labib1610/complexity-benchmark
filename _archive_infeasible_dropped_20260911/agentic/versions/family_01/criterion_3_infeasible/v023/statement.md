# Problem C — Triple-Core Resonance

Time limit: 2 s
Memory limit: 256 MB

An experimental reactor contains $n$ magnetic coils, numbered 1 to $n$. The engineers have tested various pairs of coils and recorded $m$ pairs that exhibit direct magnetic resonance. 

To achieve sustained fusion, the reactor requires a "triple-core" configuration. This configuration is formed by isolating exactly three distinct coils. When activated, energy must be able to flow directly between any two coils within this isolated group. Energy can only flow directly between two coils if they have been recorded as a resonant pair. Therefore, for the selected group of three coils to function, the recorded data must explicitly confirm resonance between the first and second coil, the first and third coil, and the second and third coil in the group.

It is guaranteed that the recorded data contains at least one such configuration. Your task is to identify it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of coils that exhibit direct magnetic resonance. The pairs are unordered, and no pair is listed more than once.
It is guaranteed that at least one valid triple-core configuration exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the identifiers of the three coils in the configuration. All three internal pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) must be present in the resonance records. Output the lexicographically smallest such triple (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
