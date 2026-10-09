# Problem A — Triple-Tally Audit

Time limit: 5 s
Memory limit: 256 MB

## Description
An auditing firm must review a historical ledger of financial interactions. There are $n$ accounts and $m$ bilateral transactions. The ledger data guarantees a specific invariant: if you scan the entire list of transactions, every account identifier from 1 to $n$ appears exactly three times in total.

The firm needs to assign each transaction to one of three available auditors (labeled 1, 2, and 3). To ensure rigorous oversight, a strict rule is enforced: no auditor is permitted to review more than one transaction involving the same account. Because every account is involved in exactly three transactions across the ledger, this rule dictates that the three transactions associated with any single account must be distributed among the three different auditors.

Determine if there is a valid assignment of the $m$ transactions to the three auditors that satisfies this oversight constraint. 

## Input
The first line has two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$).
Each of the next $m$ lines has two integers $u$ and $v$ ($1 \le u < v \le n$), representing a transaction between account $u$ and account $v$.

## Output
If a valid assignment exists, print `YES`, followed by a line with $m$ integers in $\{1, 2, 3\}$ representing the auditor assigned to each transaction in input order. If there are multiple valid assignments, any may be output.
Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
