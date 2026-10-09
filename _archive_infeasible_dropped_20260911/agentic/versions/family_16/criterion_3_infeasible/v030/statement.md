# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A computing cluster is tasked with processing a batch of $j$ sequential requests. Each request has two components: an extraction phase and a transformation phase. The cluster contains exactly two dedicated, single-threaded servers. Server 1 handles all extraction phases, while Server 2 handles all transformation phases. The system imposes a strict operational rule: a request's transformation phase cannot commence on Server 2 until its extraction phase has fully concluded on Server 1. Additionally, because the servers are single-threaded, neither server can process more than one request at a time.

All requests in the batch must be completely finished within a strict timeout threshold of $T$ milliseconds. The durations of the extraction and transformation phases for each request are known in advance.

Due to the sheer volume of the data, it is mathematically guaranteed that the batch cannot be completed within the timeout $T$, irrespective of the scheduling order chosen.

Rather than attempting to schedule the batch, your objective is to evaluate the phase durations and produce a minimal failure certificate proving that the timeout is impossible to meet. Exactly one of the following reasons will always apply. You must output the one that holds:

- **A single request is too long.** If the combined extraction and transformation durations of a specific request strictly exceed $T$, that request alone cannot finish in time.
  Print: `JOB i` — where $i$ (1-based) is the index of this request.

- **A server is overloaded.** If the sum of all durations assigned to a single server is strictly greater than $T$, the single-threaded nature of the server guarantees a timeout.
  Print: `LOAD c` — where $c$ is the server number (1 or 2) whose total load exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the durations of a request's extraction phase on Server 1 and transformation phase on Server 2, respectively.

## Output

Print a single line: `JOB i` (a request whose $p_1 + p_2$ exceeds $T$) or `LOAD c` (a server $c$ whose total load exceeds $T$).

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

In Example 1, request 1 requires 70 + 60 = 130 milliseconds in sequence. Since 130 > 100, `JOB 1` proves the timeout will be breached. 
In Example 2, no single request exceeds 150 milliseconds, but Server 1 must perform 50 + 50 + 50 + 50 = 200 milliseconds of extraction work in total. Since 200 > 150, `LOAD 1` is the certificate.
