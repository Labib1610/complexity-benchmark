# Problem A — Risk Audit

Time limit: 2 s
Memory limit: 256 MB

You are conducting a regulatory review on a sequential ledger of financial operations. The ledger consists of a total of $n$ operations, numbered sequentially from $1$ up to $n$. Your task is to classify each operation $i$ by assigning it a security tier $a_i$. The allowable security tiers are restricted to exactly the first three positive integers: $a_i \in \{1, 2, 3\}$.

The audit data includes $m$ regulatory dependencies between specific pairs of operations. To maintain strict compliance, for any dependent pair of operations, their assigned security tiers must be strictly distinct. A violation of this condition constitutes an immediate audit failure.

You must find a fully compliant security tier classification for all $n$ operations. Should multiple valid classifications exist, regulations dictate that you must provide the one that minimizes the total systemic risk penalty $P$. The risk penalty for a classification sequence $A = (a_1, a_2, \dots, a_n)$ is defined by the following evaluation:

$$P(A) = \sum_{i=1}^{n} a_i \cdot 4^{n-i}$$

If it is impossible to classify all operations without violating at least one dependency, you must declare the audit impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — representing the total number of operations and the number of regulatory dependencies, respectively.
Following this, there are $m$ lines. Each line provides two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), which indicates a regulatory dependency between operation $u$ and operation $v$.

## Output
If no compliant classification can be formed, output exactly one line containing the word `NO`.
If a valid classification exists, output `YES` on the first line. On the second line, output $n$ space-separated integers from the set $\{1, 2, 3\}$, representing the security tiers assigned to operations $1$ through $n$ in the classification that minimizes the risk penalty $P$.

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