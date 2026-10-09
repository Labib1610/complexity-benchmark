# Ledger Reconciliation

Time limit: 5 s   Memory limit: 256 MB

## Description
The central banking authority mandates that all outstanding ledger anomalies be resolved before the fiscal year ends. There are exactly $3q$ anomalies currently open, sequentially numbered from $1$ to $3q$.

To resolve these, auditors execute specific *reconciliation protocols*. Due to strict regulatory frameworks, a protocol cannot be applied to a single anomaly or an arbitrary group. Instead, every valid protocol simultaneously resolves exactly three specific anomalies.

The regulatory body has provided a master list of $t$ approved protocols. An auditor may choose to execute any selection of these approved protocols. The order of execution does not matter, but two strict rules apply to the final selection:
1. An anomaly is permanently closed once a protocol involving it is executed. Attempting to execute a protocol that references an already-closed anomaly triggers an immediate compliance violation.
2. Every single anomaly must be closed by the deadline. Leaving any anomaly open results in an audit failure.

You must determine whether it is possible to choose a selection of approved protocols that successfully closes all $3q$ anomalies without triggering any compliance violations. If such a selection exists, you must also provide it.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$): an approved protocol.

## Output
If a valid selection exists, print `YES`, then $q$ lines each with the three anomalies of one chosen protocol.
Otherwise print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
