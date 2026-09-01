# Synchronized Emitter Arrays

Time limit: 1 s
Memory limit: 256 MB

You are configuring an array of $n$ electromagnetic emitters. You must assign each emitter a base amplitude, chosen from the exact integer values $s_i \in \{1, 2\}$.

The array contains $m$ critical interference corridors. Each corridor connects a specific pair of emitters. To maintain a stable standing wave, the amplitudes assigned to any pair of emitters connected by a corridor must satisfy two safety conditions simultaneously:
1. At least one of the two connected emitters must be assigned an amplitude of 1.
2. At least one of the two connected emitters must be assigned an amplitude of 2.

You need to determine if it is possible to assign a valid amplitude to every emitter in the array such that every corridor's safety conditions are satisfied. If there are multiple valid ways to configure the array, you must output the configuration where the sequence of amplitudes $(s_1, s_2, \dots, s_n)$ is lexicographically smallest. (A sequence $A$ is lexicographically smaller than $B$ if $A$ has a smaller value at the first index where the two sequences differ.)

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), which denote the total number of emitters and the number of critical corridors, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying a critical corridor between emitter $u$ and emitter $v$.

## Output
If there is no way to assign amplitudes that satisfies all corridor constraints, output a single line with the word `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of base amplitudes.

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