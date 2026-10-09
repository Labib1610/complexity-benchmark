# Orbital Resonance

Time limit: 1 s
Memory limit: 256 MB

A deep space communications network consists of $n$ relay satellites, numbered 1 through $n$. Within this network, there are $m$ known proximity hazards. Each hazard involves a specific pair of satellites that are physically too close to one another.

To stabilize the network, every satellite $i$ must be assigned a phase state $s_i \in \{1, 2\}$. 

When a signal passes between two satellites $u$ and $v$ involved in a proximity hazard, their phase states interact to produce an interference multiplier $M_{u,v}$ for that hazard. This multiplier is calculated by taking the bitwise OR of their phase states, and adding two:
$M_{u,v} = (s_u \mid s_v) + 2$
*(Here, $\mid$ denotes the bitwise OR operation).*

The global interference level of the network is defined as the product of the interference multipliers of all $m$ listed hazards. (If there are no hazards, meaning $m=0$, this product is defined to be 1).

For the network to be safe, the global interference level must be exactly $5^m$.

Your task is to determine if there is a valid configuration of phase states for all $n$ satellites that achieves this exact global interference level. If such a configuration is possible, you must output it. 

Among all valid assignments $s_1, s_2, \dots, s_n$, output the lexicographically smallest sequence. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index $i$ where they differ, $A_i < B_i$).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a proximity hazard between satellite $u$ and satellite $v$.

## Output
If no safe configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (each being either 1 or 2), representing the phase state assigned to each satellite from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

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