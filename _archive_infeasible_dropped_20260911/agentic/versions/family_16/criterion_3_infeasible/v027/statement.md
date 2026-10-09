# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A video rendering farm processes $j$ visual effects jobs through a two-stage rendering pipeline. Every job must first be processed by the Geometry server and subsequently by the Shading server. Each server can only handle one job at a time. A job can only begin processing on the Shading server once it has completely finished on the Geometry server.

A client requires an entire batch to be completed within a strict maximum duration of $T$ seconds. The scheduling system has already determined that this deadline is impossible to meet, regardless of the execution order. Your task is to generate the appropriate rejection certificate to explain why the deadline cannot be met. 

You must output exactly one of the following formatted certificates:

- `JOB i` — The sequential processing time for job $i$ (1-based index) on both servers combined strictly exceeds $T$.
- `LOAD c` — The total processing time required by all jobs on server $c$ (where $c=1$ for Geometry, $c=2$ for Shading) strictly exceeds $T$.

It is guaranteed that exactly one valid certificate exists for every input.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200,000$, $1 \le T \le 1,000,000,000$), representing the number of jobs and the maximum allowed duration in seconds.
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1,000,000$), representing the processing time of a job on the Geometry server and the Shading server, respectively.

## Output

Print a single line containing either `JOB i` or `LOAD c`, representing the unique valid rejection certificate for the given batch.

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

In Example 1, job 1 requires $70 + 60 = 130$ seconds of sequential processing. Since $130 > 100$, `JOB 1` proves the deadline is impossible.

In Example 2, no single job exceeds 150 seconds, but the Geometry server (server 1) must process $50+50+50+50 = 200$ seconds of total work. Since $200 > 150$, `LOAD 1` is the correct certificate.
