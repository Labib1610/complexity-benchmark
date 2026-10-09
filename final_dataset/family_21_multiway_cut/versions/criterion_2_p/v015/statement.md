# Problem B — Containment Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
An underground research facility consists of $n$ distinct chambers connected by $m$ bidirectional transit tunnels. Following a safety incident, two specific chambers—designated $s$ and $t$—have been contaminated with highly reactive compounds. To prevent a catastrophic reaction, these two chambers must be completely isolated from one another. You must install physical barrier seals in a subset of the transit tunnels such that no sequence of unsealed tunnels allows air to flow between chamber $s$ and chamber $t$.

Installing a barrier in the tunnel between chamber $u$ and chamber $v$ requires a specific quantity of sealing foam, given as $w$. The total quantity of foam used is the sum of the requirements $w$ for all sealed tunnels. You have a total inventory of $B$ units of sealing foam available. The status of the remaining $n-2$ chambers is irrelevant to the safety protocol; they may remain connected to either $s$, $t$, or neither, provided $s$ and $t$ are mutually isolated.

Determine if it is possible to achieve this isolation without exceeding the available inventory $B$. If it is achievable, provide a valid barrier deployment plan.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$: the number of chambers, the number of tunnels, the identifiers of the two contaminated chambers, and the total sealing foam budget.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a bidirectional tunnel between chamber $u$ and chamber $v$ that requires $w$ units of foam to seal.

## Output
If the isolation is possible within the budget, print `YES` on the first line. On the second line, print an integer $c$ representing the number of tunnels to seal. On each of the next $c$ lines, print two integers $u$ and $v$ identifying a tunnel to be sealed. If multiple valid plans exist, any plan that does not exceed the budget is acceptable.
If it is impossible to isolate the chambers within the budget, print `NO`.

## Example

### Input
```
5 6 1 5 10
1 2 4
1 3 5
2 4 6
3 4 3
2 5 5
4 5 4
```

### Output
```
YES
2
1 2
3 4
```
