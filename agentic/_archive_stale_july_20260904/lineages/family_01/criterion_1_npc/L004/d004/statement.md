# Signal Separation Protocols

**Time limit:** 2 s  
**Memory limit:** 256 MB  

You manage an array of $n$ signal emitters, numbered from $1$ to $n$. Each emitter must operate on a single frequency mode. There are exactly three available frequency modes, denoted by the integers $1$, $2$, and $3$.

Interference occurs if certain emitters share the same mode. You are provided with a list of $m$ critical pairs of emitters. For each critical pair $(u, v)$, their respective frequency modes $f_u$ and $f_v$ must be separated by at least one unit, meaning $|f_u - f_v| \ge 1$. The critical pairs can link any subsets of emitters in arbitrary arrangements, and all $m$ separation requirements must be simultaneously fulfilled.

Your task is to determine if a complete, valid mode configuration can be established for all $n$ emitters such that no critical pair violates the separation rule.

## Input
The first line consists of two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$), which represent the total number of emitters and the total number of critical pairs.
Each of the following $m$ lines provides two integers $u$ and $v$ (indices from $1$ to $n$), identifying a pair of emitters that are subject to the separation rule.

## Output
If there is no way to configure the emitters without violating the rules, output `NO` on a single line.
If a valid assignment is achievable, output `YES` on the first line. On the second line, provide a sequence of $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$) representing the frequency mode for each emitter $i$. If more than one valid sequence exists, you must output the lexicographically smallest sequence (comparing the mode for emitter $1$ first, then emitter $2$, and so on up to emitter $n$).

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```