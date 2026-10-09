# Problem A — Risk Audit

Time limit: 2 s
Memory limit: 256 MB

You are auditing a ledger of sequential financial transactions. The ledger contains $n$ transactions, indexed from $1$ to $n$. For each transaction $i$, you must assign a risk tier $c_i$. There are exactly three risk tiers available, represented by the values $1$, $2$, and $3$.

The ledger also specifies $m$ dependency links between certain transactions. Due to regulatory rules, any two transactions connected by a dependency link must not be assigned the same risk tier. If any linked pair shares the same risk tier, it triggers a compliance violation.

Your objective is to determine a compliant risk configuration for the entire ledger. If there is more than one compliant configuration, you must output the one that is lexicographically smallest. A configuration sequence $A = (a_1, a_2, \dots, a_n)$ is lexicographically smaller than sequence $B = (b_1, b_2, \dots, b_n)$ if, at the first index $i$ where they differ, $a_i < b_i$.

If there is no way to assign the risk tiers without a compliance violation, you must report that the configuration is impossible.

*System Note:* The automated test cases include dependency structures specifically constructed so that many partial assignments of tiers to a prefix of transactions are locally valid but possess no fully compliant extension to the entire ledger. 

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of transactions and the number of dependency links.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that a dependency link connects transaction $u$ and transaction $v$.

## Output
If a compliant configuration is impossible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers from the set $\{1, 2, 3\}$, representing the assigned risk tiers for transactions $1$ through $n$ in the lexicographically smallest compliant configuration.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
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
NO
```