# Problem C — Concurrency Fallback Trigger

Time limit: 2 s   Memory limit: 256 MB

A database system is attempting to process a batch of concurrent transactions. Certain pairs of transactions have overlapping write requests and cannot be executed in the same batch processing thread.

The current set of transactions cannot be scheduled using the standard two-thread pool. To trigger the fallback execution mode, you must provide a minimal proof of this scheduling impossibility. You do not need to attempt a safe schedule yourself.

Specifically, you must identify three distinct transaction IDs, $a$, $b$, and $c$, such that the system logs an overlap for $a$ and $b$, an overlap for $b$ and $c$, and an overlap for $a$ and $c$. Because these three specific overlaps prevent any two of the three transactions from sharing a thread, they prove that at least three threads are required.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of transactions and the number of overlapping pairs. Transactions are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that an overlap exists between transaction $u$ and transaction $v$.
It is guaranteed that the batch contains at least one set of three transactions satisfying the fallback criteria.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three transactions that form the proof.
If there are multiple valid sets of three transactions, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```