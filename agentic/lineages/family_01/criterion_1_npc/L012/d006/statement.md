# Problem A — Risk Audit

Time limit: 2 s
Memory limit: 256 MB

You are auditing a ledger of $n$ sequential financial transactions, indexed from $1$ to $n$. For each transaction $i$, you must assign a risk tier $c_i$. There are exactly three risk tiers available, represented by the values $1$, $2$, and $3$.

The ledger contains $m$ dependency links. Each link specifies a pair of transactions. Due to regulatory rules, for every such pair, the set of risk tiers assigned to the two transactions must contain exactly two distinct values. If this condition fails for any link, it triggers a compliance violation.

Your objective is to determine a compliant risk configuration for the entire ledger. If there is more than one compliant configuration, you must output the one that yields the minimum possible value for the audit hash, which is calculated using the formula:
$$ \sum_{i=1}^{n} c_i \cdot 2^{2n - 2i} $$
If there is no way to assign the risk tiers without a compliance violation, you must report that the configuration is impossible.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of transactions and the number of dependency links.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that a dependency link connects transaction $u$ and transaction $v$.

## Output
If a compliant configuration is impossible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers from the set $\{1, 2, 3\}$, representing the risk tiers for transactions $1$ through $n$ that minimize the audit hash.

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