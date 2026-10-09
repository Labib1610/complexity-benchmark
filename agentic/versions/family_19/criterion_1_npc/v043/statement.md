# Problem A — Ledger-Balanced Freight Assignments

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics system consists of $n$ distribution centers. Between certain pairs of centers, there are one-way shipping lanes. Each shipping lane has a strict maximum allowance, which is the highest combined count of crates it can process during a single operational cycle.

During the upcoming cycle, $k$ independent delivery orders must be fulfilled. Each order $i$ dictates that a net total of $d_i$ crates must be dispatched from a starting center $s_i$ and collected at a final destination center $t_i$. 

To track this, every distribution center maintains a separate ledger balance for each order. For a specific order, a center's ledger balance is calculated as the total number of crates for that order routed out of the center via shipping lanes, minus the total number of crates for that order routed into the center via shipping lanes. To successfully fulfill order $i$, its ledger balance must be exactly $+d_i$ at center $s_i$, exactly $-d_i$ at center $t_i$, and exactly $0$ at all other centers.

Crates cannot be fractionally divided; the number of crates assigned to any lane for any order must be a non-negative integer. Crates from different orders are assigned simultaneously. Consequently, for any given shipping lane, the sum of crates from all orders assigned to that lane cannot exceed its maximum allowance.

You need to determine if there is an assignment of crates to shipping lanes that satisfies all ledger requirements for all orders without exceeding any lane's allowance. If such an assignment exists, provide a detailed breakdown of how many crates from each order are allocated to each shipping lane.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of distribution centers, shipping lanes, and delivery orders, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the starting center, the final destination center, and the required volume of crates $d_i$ for the $i$-th order.
The following $m$ lines each describe a one-way shipping lane with three integers $u$, $v$, and $c$, indicating a lane from center $u$ to center $v$ with a maximum allowance of $c$ crates.

## Output
If a valid assignment exists, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines should contain $m$ integers, where the $j$-th integer represents the number of crates belonging to the $i$-th order routed over the $j$-th shipping lane (in the order lanes are given in the input).
If no such assignment is possible, print `NO`.

## Example

### Input
```text
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 4 1
3 4 1
2 3 1
```

### Output
```text
YES
1 0 1 0 0
0 0 0 0 1
```
