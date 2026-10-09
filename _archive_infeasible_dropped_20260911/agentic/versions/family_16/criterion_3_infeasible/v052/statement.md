# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are auditing a cloud computing platform that has been assigned $j$ data processing jobs. Every job must be sequentially processed by two distinct microservices: the Extraction Service (Service 1) and the Formatting Service (Service 2). You are given the processing time each job requires on Service 1 and Service 2.

The system architecture enforces the following constraints:
- A job can only be routed to the Formatting Service after it has fully completed its processing in the Extraction Service.
- The Extraction Service is single-threaded and can process only one job at a time.
- The Formatting Service is single-threaded and can process only one job at a time.
- The entire batch of $j$ jobs must be fully processed by both services within a strict timeout window of $T$ milliseconds.

For every test case, it is guaranteed that the $T$ millisecond timeout will inevitably be exceeded, regardless of the scheduling strategy used. Your task is not to find a valid execution schedule, but to output a short certificate proving that the timeout is impossible to meet.

Exactly one of the following two failure conditions will apply to the provided data. Output the certificate for the condition that holds:

- **Single Job Violation**: A specific job requires a combined processing time across both services that strictly exceeds $T$, meaning it would fail to finish even if it were the only job in the system. Print `JOB i`, where $i$ is the 1-based index of such a job.
- **Service Overload**: A specific service has an aggregate workload (the sum of processing times for all $j$ jobs on that service) that strictly exceeds $T$, meaning that service alone cannot finish its queue before the timeout. Print `LOAD c`, where $c$ is 1 (for the Extraction Service) or 2 (for the Formatting Service).

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200000, 1 ≤ $T$ ≤ 1000000000).
The following $j$ lines each contain two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1000000), representing the requested processing time of the job on the Extraction Service and the Formatting Service, respectively.

## Output

Print a single line containing either `JOB i` (if the sum of $p_1$ and $p_2$ for job $i$ exceeds $T$) or `LOAD c` (if the sum of processing times for all jobs on service $c$ exceeds $T$).

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

In Example 1, the first job requires 70 + 60 = 130 milliseconds in sequence. Since 130 > 100, `JOB 1` proves the timeout is impossible to meet. 
In Example 2, no single job exceeds 150 milliseconds. However, the Extraction Service must process 50 + 50 + 50 + 50 = 200 milliseconds of work in total. Since 200 > 150, `LOAD 1` serves as the certificate.
