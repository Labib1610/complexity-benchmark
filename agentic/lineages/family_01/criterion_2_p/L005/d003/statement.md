# Problem B — Market Reconciliation

Time limit: 1 s   Memory limit: 256 MB

A commodities exchange is auditing $n$ market participants. The exchange has a record of $m$ bilateral contracts, each occurring between a specific pair of participants.

To reconcile the ledger, the exchange must determine the market role of each participant. Each participant must be assigned a single role for the entire audit period: either 1 (representing a buyer) or 2 (representing a seller). For any bilateral contract to be valid, it must involve exactly one buyer and one seller. Therefore, the role values of the two participants involved in any contract must sum to exactly 3.

You must find a role assignment for all participants that validates every recorded contract. If the ledger cannot be reconciled under these rules, indicate that it is impossible.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of participants and bilateral contracts, respectively.
The following $m$ lines each contain two integers $u$ and $v$ — a pair of participants who entered into a bilateral contract.

## Output
If the ledger cannot be reconciled, output NO on a single line.
If it can, output YES on the first line. On the second line, output $n$ integers $r_1 \dots r_n$ (each in {1,2}), representing the lexicographically smallest valid sequence of roles for participants $1$ through $n$.

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