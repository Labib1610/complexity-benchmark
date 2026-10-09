# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A data center must resolve **j** queries. Each query requires sequential execution: it must first complete a data retrieval phase on the storage array (Component 1), and subsequently complete an analysis phase on the compute node (Component 2). For each query, you are given the exact number of minutes required on Component 1, and the exact number of minutes required on Component 2. 

The system operates under strict concurrency limits:
- A query can only begin its Component 2 phase after its Component 1 phase is entirely complete.
- The storage array (Component 1) can process at most one query at any given moment.
- The compute node (Component 2) can process at most one query at any given moment.
- All queries must be completely finished by time **T**.

For every input in this problem, it is **guaranteed that the deadline cannot be met**, no matter how the system schedules the queries. Your task is not to search for a schedule; it is to **prove** the deadline is impossible by identifying a hypothetical relaxation of the system constraints that *still* fails to meet the deadline. 

It is guaranteed that exactly one of the following three relaxed scenarios will inevitably fail to finish by time **T** (while the remaining two could theoretically be completed by time **T** in their relaxed states). Output the certificate for the unique scenario that fails:

- **Relaxed Scenario A:** All queries except query **i** (for a specific 1-based index **i**) are cancelled. Query **i** is processed alone under the original rules. If this single query cannot finish by time **T**, print `JOB i`.
- **Relaxed Scenario B:** The compute node (Component 2) is infinitely fast, requiring 0 minutes for all queries. The storage array (Component 1) retains its original constraint: it can process at most one query at any given moment. If, under these conditions, the queries cannot all finish by time **T** regardless of the chosen schedule, print `LOAD 1`.
- **Relaxed Scenario C:** The storage array (Component 1) is infinitely fast, requiring 0 minutes for all queries. The compute node (Component 2) retains its original constraint: it can process at most one query at any given moment. If, under these conditions, the queries cannot all finish by time **T** regardless of the chosen schedule, print `LOAD 2`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required minutes of the query on Component 1 and Component 2.

## Output

Print a single line containing the certificate:
- `JOB i` (where **i** is the 1-based query index for which Relaxed Scenario A fails)
- `LOAD c` (where **c** is 1 if Relaxed Scenario B fails, or 2 if Relaxed Scenario C fails)

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, under Relaxed Scenario A for query 1, processing query 1 alone requires 70 minutes on Component 1 followed by 60 minutes on Component 2. This sequence cannot be completed by time 100, so `JOB 1` proves the deadline is impossible.

In Example 2, no single query fails Relaxed Scenario A. However, under Relaxed Scenario B, even if Component 2 takes 0 time, processing all four queries on Component 1 (which can only process one query at a time) requires a minimum of 200 minutes. This cannot be completed by time 150, making `LOAD 1` the certificate.