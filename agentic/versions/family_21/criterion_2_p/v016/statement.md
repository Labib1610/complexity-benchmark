# Problem B — Sealing Two Sites Apart

Time limit: 2 s
Memory limit: 256 MB

## Description
An underground research complex consists of $n$ chambers connected by $m$ links. Each link has an associated closure cost, representing the resources required to permanently block it. Two specific chambers, designated as $s$ and $t$, contain volatile materials that must be strictly quarantined from each other. To achieve this, a subset of links must be selected for permanent removal such that no continuous sequence of unremoved links connects chamber $s$ to chamber $t$ in either direction. A removed link permits no passage whatsoever.

Chambers other than $s$ and $t$ can remain accessible to either $s$, $t$, or neither. The total expenditure for the quarantine operation is exactly the sum of the closure costs of the removed links. You are given a maximum budget $B$ for this operation.

Furthermore, any valid quarantine plan must adhere to the following operational limits:
- The total number of removed links must not exceed $m$.
- The combined closure cost of the removed links must not exceed the sum of the closure costs of all $m$ links in the complex.

Determine a set of links to remove such that the total expenditure is at most $B$ and the two volatile chambers are separated, or determine that no such plan exists within the budget.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$.
The next $m$ lines each contain three integers $u$, $v$, and $w$, representing a link between chamber $u$ and chamber $v$ with closure cost $w$.

## Output
If a valid plan exists, print `YES` on the first line. On the second line, print the number of removed links $c$. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a removed link.
If no such plan exists within the budget, print `NO`.

## Example

**Input**
```text
4 5 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
2 3 2
```

**Output**
```text
YES
2
2 4
3 4
```
