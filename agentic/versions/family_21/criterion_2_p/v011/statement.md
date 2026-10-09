# Problem B — Severing the Arbitrage Loop

Time limit: 2 s   Memory limit: 256 MB

## Description
A regulatory body is investigating a network of trading accounts. Pairs of accounts are linked by automated transfer protocols that allow funds to move freely back and forth between them. Canceling a protocol incurs a specific contractual penalty.

The investigators have identified two primary accounts that are exploiting a regulatory loophole. To stop this, the agency must ensure that these two accounts can no longer exchange funds. Specifically, they must cancel a set of transfer protocols such that it becomes impossible to move funds from the first account to the second, or vice versa, through any sequence of remaining active protocols. 

The agency does not care if other accounts are isolated or grouped together as a result of the cancellations, as long as the two primary accounts end up completely separated from each other. However, the agency has a strict maximum limit on the total penalties they can incur from canceling protocols. 

Determine a set of transfer protocols to cancel that successfully isolates the two primary accounts without exceeding the maximum penalty limit, or state if it is impossible to do so within the limit.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$. $n$ is the total number of accounts (numbered $1$ to $n$), $m$ is the number of transfer protocols, $s$ and $t$ are the identifiers of the two primary accounts, and $B$ is the penalty limit.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating an automated transfer protocol between account $u$ and account $v$ with a cancellation penalty of $w$.

## Output
If the separation can be achieved within the limit, print `YES` on the first line. On the second line, print the number of canceled protocols, $c$. Then, output $c$ lines, each containing two integers $u$ and $v$, representing a canceled protocol between account $u$ and account $v$. 
If the penalty limit is insufficient to separate the accounts, print `NO`.

## Example 1

**Input**
```text
4 4 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
```

**Output**
```text
YES
2
1 2
3 4
```

## Example 2

**Input**
```text
4 4 1 4 5
1 2 4
1 3 5
2 4 6
3 4 3
```

**Output**
```text
NO
```
