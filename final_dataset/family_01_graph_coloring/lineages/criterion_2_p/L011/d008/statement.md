# Continuous Band Allocation

Time limit: 1 s
Memory limit: 256 MB

A research facility operates a network of $n$ wideband transmitters. To maintain operational stability, every transmitter $i$ ($1 \le i \le n$) must be assigned a fixed continuous operational band $I_i$. This band must be chosen from the set of two closed real intervals: $\{[0, 1], [1, 2]\}$.

The facility's layout dictates $m$ spacing requirements. Each requirement specifies two transmitters $u$ and $v$. To prevent resonant interference, the union of the operational bands assigned to these two transmitters must form an interval of length exactly 2. That is, for every specified pair, the set $I_u \cup I_v$ must be an interval of length 2. A configuration is only valid if this condition holds for all $m$ requirements simultaneously.

Your objective is to determine if a viable sequence of operational bands $(I_1, I_2, \dots, I_n)$ exists. If multiple valid sequences are possible, you must output the sequence that yields the lexicographically smallest sequence of right endpoints. 

For an interval $[a, b]$, the right endpoint is $b$. Thus, you will output a sequence of $n$ integers, each being either $1$ or $2$. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index where they differ, $A$ has a smaller value than $B$. This prioritization applies globally across the entire sequence of $n$ transmitters.)

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200,000$, $0 \le m \le 200,000$), representing the number of transmitters and the number of requirements, respectively.

Each of the next $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that the requirement regarding the length of $I_u \cup I_v$ must hold for transmitters $u$ and $v$.

## Output
If it is impossible to find a viable assignment of operational bands, output `NO` on a single line.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers representing the sequence of right endpoints of $I_1, I_2, \dots, I_n$. This sequence must be the lexicographically smallest valid sequence of right endpoints.

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