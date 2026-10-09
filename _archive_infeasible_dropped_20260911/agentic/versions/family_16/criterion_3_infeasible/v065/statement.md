# System Validation Script

Time limit: 2 s   Memory limit: 256 MB

## Description

A server must process $j$ jobs through two sequential phases: Phase 1 and Phase 2. The server operates for a single continuous window of $T$ milliseconds. Each job must complete Phase 1 before it can begin Phase 2.

Before any execution begins, a validation script checks for basic capacity errors. The script will raise an error if:

- A single job requires more than $T$ milliseconds total across both phases. If this occurs for job $i$ (1-indexed), the script outputs `JOB i`.
- A phase requires more than $T$ milliseconds of total processing time across all jobs combined. If this occurs for phase $c$ (1 or 2), the script outputs `LOAD c`.

The input data is structured such that exactly one of these validation errors will be raised. Your task is to determine which error the script will output.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$), representing the processing times of a job in Phase 1 and Phase 2, respectively.

## Output

Print a single line containing either `JOB i` or `LOAD c`, corresponding to the validation error that is raised.

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

In Example 1, the first job requires $70 + 60 = 130$ milliseconds. Since $130 > 100$, the script outputs `JOB 1`.
In Example 2, no individual job exceeds 150 milliseconds. However, Phase 1 requires $50 + 50 + 50 + 50 = 200$ milliseconds in total. Since $200 > 150$, the script outputs `LOAD 1`.
