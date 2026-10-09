# Problem B — Configuration Space of Loom Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
An industrial loom executes a weaving pattern defined by $m$ discrete operations. We define a schedule as an assignment of these $m$ operations to discrete machine cycles.

Let $\Delta$ be the maximum number of operations that involve any single feed. The machine must execute the entire pattern in exactly $\Delta$ cycles. Thus, a schedule is a sequence of $m$ integers $(c_1, c_2, \dots, c_m)$ where each $c_i \in \{1, 2, \dots, \Delta\}$. The schedule space contains exactly $\Delta^m$ distinct sequences.

A schedule is valid if it satisfies the feed-exclusion constraints: no single feed may be involved in more than one operation assigned to the same cycle $c$. Each operation involves exactly two feeds: one longitudinal warp feed and one transverse weft feed. Operations never involve a pair of warp feeds nor a pair of weft feeds.

Your task is to search the space of $\Delta^m$ possible sequences to find a valid schedule. The architectural rules of the loom ensure that the set of valid sequences is strictly non-empty.

## Input
The first line contains three integers `nL`, `nR`, and `m` ($1 \le \text{nL}, \text{nR} \le 100000$, $0 \le m \le 400000$), representing the number of warp feeds, the number of weft feeds, and the total number of operations, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le \text{nL}$, $1 \le v \le \text{nR}$), indicating that an operation involves warp feed $u$ and weft feed $v$.

## Output
Print `YES` on the first line.
On the second line, output $m$ space-separated integers representing a valid schedule sequence. The $i$-th integer corresponds to the cycle $c_i$ assigned to the $i$-th operation in the input order. If multiple valid sequences exist, output any of them.

## Example
### Input
```
4 4 6
1 1
1 2
2 2
2 3
3 3
4 3
```
### Output
```
YES
1 2 1 2 1 3
```
