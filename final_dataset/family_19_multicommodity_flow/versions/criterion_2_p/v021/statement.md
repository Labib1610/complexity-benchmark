# Problem B — Distributed Ledger Liquidity Routing

Time limit: 2 s
Memory limit: 256 MB

## Description
A decentralized financial network needs to execute a large aggregated settlement. The network consists of $n$ participant accounts and $m$ established unidirectional trust lines. A single asset type (denoted by the constant `1` in the configuration) is being moved.

A specific settlement requires transferring exactly $d$ units of this asset from a sending account $s$ to a receiving account $t$. The transfer must happen within a single settlement window. 

Each trust line from account $u$ to account $v$ has a maximum liquidity limit, meaning it can process at most $cap$ units of the asset during this window. The amount assigned to each trust line must be a non-negative whole number. 

For all accounts other than $s$ and $t$, the total amount of the asset received from incoming trust lines must exactly equal the total amount sent out through outgoing trust lines. These intermediate accounts act only as transit relays and cannot absorb or produce any units of the asset. The net amount leaving $s$ and the net amount arriving at $t$ must both be exactly $d$. 

Determine a valid assignment of transfer amounts for each trust line that satisfies all liquidity limits and relay conditions, achieving the exact required transfer $d$. If no such assignment is possible, report that the settlement cannot be executed.

## Input
Line 1: Three integers $n$, $m$, and $1$.
Line 2: Three integers $s$, $t$, and $d$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, indicating a trust line from account $u$ to account $v$ with a liquidity limit of $cap$.

## Output
If the settlement can be executed, output `YES` on the first line. On the second line, output $m$ space-separated integers representing the transfer amount assigned to each trust line, in the exact order they were provided in the input. (If multiple valid assignments exist, any will be accepted).
If it cannot be executed, output `NO`.

## Example

**Input:**
```
4 4 1
1 4 7
1 2 5
1 3 2
2 4 5
3 4 2
```

**Output:**
```
YES
5 2 5 2
```
