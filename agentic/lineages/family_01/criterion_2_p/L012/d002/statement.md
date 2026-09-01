# Sensor Polarity Configuration

Time limit: 1 s
Memory limit: 256 MB

You are tasked with calibrating a network containing $n$ sensors. You must assign each sensor an operational mode, chosen from the integer values $s_i \in \{1, 2\}$.

The network contains $m$ critical links between specific pairs of sensors. To prevent interference, any two sensors $(u, v)$ connected by a critical link must be configured such that the bitwise AND of their operational modes is exactly zero ($s_u \ \& \ s_v = 0$).

You need to determine if it is possible to assign a valid mode to every sensor in the network without violating the interference constraint on any critical link. If there are multiple valid ways to configure the network, you must output the configuration where the sequence of modes $(s_1, s_2, \dots, s_n)$ is lexicographically smallest. (A sequence $A$ is lexicographically smaller than $B$ if $A$ has a smaller value at the first index where the two sequences differ.)

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), which denote the total number of sensors and the number of critical links, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying a critical link between sensor $u$ and sensor $v$.

## Output
If there is no way to assign modes that satisfies all link constraints, output a single line with the word `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of operational modes.

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