# Problem C — Impossibility Evidence

Time limit: 2 s
Memory limit: 256 MB

## Description

A system must process $j$ sequential data requests. Every request must be fully processed by Node 1, and immediately after completion, it must be processed by Node 2. You are provided the duration each request requires at Node 1 and at Node 2. Each node operates strictly sequentially, handling at most one request at any given moment.

An overarching time limit $T$ has been established; all requests must be completely finished by time $T$.

For all test cases evaluated here, it is guaranteed that this time limit cannot be satisfied, regardless of the chronological order in which the requests are handled. Your objective is not to find an ordering, but to output a precise string that proves the limit is strictly broken.

Based on the input, exactly one of the following two failure conditions will be true. You must print the corresponding evidence code:

- **Individual request breach:** If a single request's combined duration (its time at Node 1 plus its time at Node 2) is strictly greater than $T$, that request alone cannot finish within the limit.
  Print: `JOB i` — where $i$ (1-based index) is such a request.

- **Node capacity breach:** Because a node operates sequentially, it must be active for the sum of all durations assigned to it. If the total duration of all requests at Node 1 (or Node 2) is strictly greater than $T$, the limit cannot be met.
  Print: `LOAD c` — where $c$ is 1 or 2, representing a node whose total sum of durations exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the durations required for the request at Node 1 and Node 2, respectively.

## Output

Print a single line: `JOB i` (for a request whose $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a node $c$ whose total sum of durations exceeds $T$).

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

In Example 1, the first request requires $70 + 60 = 130$ units of time in sequence. Since $130 > 100$, the code `JOB 1` proves the time limit is broken.
In Example 2, no single request exceeds 150 units of time, but Node 1 must be active for $50+50+50+50 = 200$ units. Since $200 > 150$, the code `LOAD 1` is the correct evidence.
