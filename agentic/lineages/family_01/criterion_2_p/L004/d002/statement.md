# Orbital Resonance

Time limit: 1 s
Memory limit: 256 MB

A deep space communications network consists of $n$ relay satellites, numbered 1 through $n$. Within this network, there are $m$ known proximity hazards. Each hazard involves a specific pair of satellites that are physically too close to one another.

Every satellite in the network must be assigned a tuning parameter, which is an integer chosen from $\{1, 2\}$. Whenever two satellites are involved in a proximity hazard, the absolute difference between the cubes of their tuning parameters must be exactly 7 to maintain orbital equilibrium. If this difference evaluates to any other value, their resonance will cause a system-wide failure.

Your task is to determine if there is a valid configuration of tuning parameters for all $n$ satellites that prevents any system-wide failures. If such a configuration is possible, you must output it. If there are multiple valid ways to assign the parameters, you must choose the one whose sequence of assignments $s_1, s_2, \dots, s_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a proximity hazard between satellite $u$ and satellite $v$.

## Output
If no safe configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (each being either 1 or 2), representing the tuning parameter assigned to each satellite from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

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