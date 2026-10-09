# SLA Rejection Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing platform uses a two-stage pipeline to process client requests. A batch of $j$ requests has been submitted. Every request must be processed on machine 1 and then on machine 2. Each machine processes one request at a time without preemption. A request can only begin on machine 2 after it has completely finished on machine 1.

The client requires all $j$ requests to be completely finished by a deadline of $T$ milliseconds. 

For every input provided, it is impossible to meet this deadline. The input guarantees that exactly one of the two following limitation categories applies. You must print a short rejection certificate from the applicable category:

- **Isolated Job Obstruction:** There is a request that would fail to complete by the deadline even if it were the only request in the system (i.e., experiencing zero wait time for either machine). If this category applies, print `JOB i` (where $i$ is the 1-based index of the request). If multiple requests satisfy this, printing any one of them is acceptable.

- **Continuous Utilization Exhaustion:** There is a machine that would fail to finish its assigned operations by the deadline even if it never experienced any idle time from time 0 onwards. If this category applies, print `LOAD c` (where $c \in \{1, 2\}$ is the machine number). If both machines satisfy this, printing either is acceptable.

Output must be consistent with the unique applicable limitation category guaranteed by the input.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the processing times of a request on machine 1 and machine 2, respectively.

## Output

Print a single line containing either `JOB i` (for a request qualifying under the Isolated Job Obstruction) or `LOAD c` (for a machine qualifying under the Continuous Utilization Exhaustion). The output must be consistent with the unique applicable limitation category guaranteed by the input.

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

In Example 1, request 1 requires 70 ms on machine 1 and 60 ms on machine 2. Even if it were the only request in the system, it would require 130 ms to complete, which exceeds the 100 ms deadline. Thus, the Isolated Job Obstruction category applies, and `JOB 1` is a valid rejection certificate.

In Example 2, machine 1 must process four requests requiring 50 ms each. Even running continuously from time 0, it would require 200 ms to finish all its operations, which exceeds the 150 ms deadline. No individual request exceeds the deadline on its own, but the Continuous Utilization Exhaustion category applies, and `LOAD 1` is a valid rejection certificate.