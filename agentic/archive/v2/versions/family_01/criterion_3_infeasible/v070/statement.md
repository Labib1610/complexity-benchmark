# System Log Audit: Identifying Mutually Interlocking Transaction Sets

Time limit: 2 s   Memory limit: 256 MB

In a distributed transaction coordinator, $n$ active transaction threads are assigned integer identifier tags from $1$ to $n$. During high-concurrency execution, static analysis of execution logs flags pairwise resource collisions between specific transactions. To isolate a minimal deadlocked execution state for offline root-cause analysis, the auditing module must find three distinct transaction tags $a$, $b$, and $c$ (with $a < b < c$) that form a mutually interlocking group—meaning every pair among $a$, $b$, and $c$ experiences a direct resource collision.

To ensure identical error reporting across independent audit nodes, if multiple such triplets exist, the module must select the lexicographically smallest triplet. Specifically, choose a valid triplet $(a, b, c)$ that minimizes $a$; if there are ties, minimize $b$; and if ties still remain, minimize $c$.

It is guaranteed that at least one mutually interlocking triplet exists in the log data.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of active transaction identifiers and the total number of flagged pairwise collisions, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pairwise collision between transaction $u$ and transaction $v$.

## Output
Print three space-separated integers $a\ b\ c$ on a single line with $a < b < c$, representing the transaction tags of the lexicographically smallest mutually interlocking triplet.

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
