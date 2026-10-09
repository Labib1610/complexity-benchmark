# Problem B — Securing the Complex

Time limit: 2 s
Memory limit: 256 MB

## Description
An underground facility consists of $n$ chambers connected by $m$ tunnels. Each tunnel carries a designated demolition cost, representing the explosives and labour required to collapse it permanently. Two specific chambers, designated as $s$ and $t$, contain volatile substances that must never be allowed to mix. Following the safety intervention, there must be no remaining sequence of intact tunnels that allows passage between chamber $s$ and chamber $t$. A collapsed tunnel permits no transfer of material in either direction.

Chambers other than $s$ and $t$ may remain connected to either of the two volatile chambers; their final connectivity does not affect the safety compliance of the plan. The sole metric evaluated is the total demolition cost, which is the sum of the costs of the tunnels that are actually collapsed. The facility administrators have allocated a fixed budget $B$ that this total must not exceed.

Determine a set of tunnels to collapse such that their total cost is within the budget $B$ and their removal leaves chambers $s$ and $t$ completely isolated from one another. If multiple valid sets exist, any may be chosen. If no such set of tunnels can be collapsed without exceeding the budget, you must report that the intervention is impossible.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$: the number of chambers, the number of tunnels, the identifiers of the two volatile chambers, and the maximum allowed budget.
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating a tunnel between chamber $u$ and chamber $v$ with a demolition cost of $w$.

## Output
If a valid intervention exists, print `YES` on the first line. On the second line, print an integer $c$ representing the number of collapsed tunnels. On each of the next $c$ lines, print two integers $u$ and $v$ representing a tunnel to collapse.
If no valid intervention exists within the budget, print `NO`.

## Example

### Input
```
4 4 1 4 10
1 2 5
1 3 5
2 4 4
3 4 7
```

### Output
```
YES
2
2 4
1 3
```
