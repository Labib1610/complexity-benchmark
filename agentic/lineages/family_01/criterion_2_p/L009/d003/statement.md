# Problem B — Flux Channels

Time limit: 1 s   Memory limit: 256 MB

An experimental fusion reactor contains $n$ magnetic coils. Each coil $i$ must be tuned to an operating frequency multiplier $c_i$, which must be chosen from the set $\{1, 2\}$.

The reactor's design includes $m$ delicate flux channels, each connecting a specific pair of coils. To maintain a stable magnetic field and prevent the channel from saturating, the sum of the frequency multipliers of the two coils connected by any flux channel must be exactly 3.

You need to determine if there is a valid tuning for all $n$ coils that keeps every flux channel stable, or report that no such configuration is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of coils connected by a flux channel.

## Output
If no valid tuning exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $c_1, \dots, c_n$, where $c_i$ is the frequency multiplier assigned to coil $i$. If there are multiple valid sequences of multipliers, choose the sequence that minimizes $c_1$. If there is still a tie, minimize $c_2$ among the remaining valid sequences, and continue this process up to $c_n$.

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