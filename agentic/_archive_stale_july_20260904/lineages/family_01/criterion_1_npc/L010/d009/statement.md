# Problem A — Resonant Loop Prevention

Time limit: 2 s
Memory limit: 256 MB

You are configuring a system of $n$ signal relays, numbered 1 to $n$. Each relay must be assigned a frequency multiplier chosen from the values 1, 2, and 3. This configuration is expressed as a sequence $f_1, f_2, \dots, f_n$.

You are provided with a list of $m$ pairs of relays that are in physical proximity. Proximity is a symmetric relationship. 

For each pair of relays $u$ and $v$ that are in physical proximity, we analyze their combined signal. The connection between them is perfectly stable if and only if the sum of their cubed multipliers is strictly greater than the product of their sum and their product. In mathematical terms:
$$f_u^3 + f_v^3 > (f_u + f_v) f_u f_v$$

The system is perfectly stable if and only if every pair of relays in physical proximity forms a stable connection.

Your task is to determine if there exists a valid sequence of multipliers such that the system is perfectly stable. If such a sequence exists, you must output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that relay $u$ and relay $v$ are in physical proximity.

## Output
If there is no valid sequence of multipliers that makes the system stable, print a single line containing `NO`.
If at least one such sequence exists, print `YES` on the first line. On the second line, print the $n$ integers $f_1, f_2, \dots, f_n$ representing the multipliers assigned to the relays. 
If there are multiple valid sequences, you must output the one that is lexicographically smallest. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index $i$ where they differ, $A_i < B_i$).

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