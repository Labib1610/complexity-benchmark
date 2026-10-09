# Refinery Contract Rejection

Time limit: 2 s   Memory limit: 256 MB

## Description

A data refinery operates a sequential two-phase purification process. A batch of $j$ jobs has been submitted. To ensure integrity, every job must first be completely analyzed in phase 1, and only then can it be analyzed in phase 2. Each phase is handled by a dedicated system that can only process one job at any given moment.

The customer demands that all $j$ jobs finish both phases within a strict timeframe of $T$ milliseconds.

For every input in this problem, the requested timeframe is guaranteed to be impossible to meet, regardless of how the jobs are scheduled. Your task is to generate a short rejection certificate that proves the timeframe is impossible, which can be verified directly against the input.

Exactly one of the following rejection reasons will always apply. Output the one that holds:

- **Individual job bottleneck.** If a specific job's processing durations in both phases add up to more than $T$, that job alone (running through phase 1 then phase 2 sequentially) cannot finish by $T$.
  Output: `JOB i` — where `i` (1-based index) is the job in question.

- **Phase congestion.** Because each phase processes jobs one after another, a phase requires a time span at least equal to the sum of all its processing durations. If the total processing duration required for phase 1 (or phase 2) exceeds $T$, the timeframe is impossible.
  Output: `LOAD c` — where `c` is 1 or 2, representing the phase whose total processing duration exceeds $T$.

## Input

The first line contains two integers $j$ and $T$. The batch size $j$ is at least $1$ and will not exceed the exact number of seconds in $55$ hours, $33$ minutes, and $20$ seconds. The timeframe $T$ is at least $1$ and will at most equal the number of millimeters in exactly one thousand kilometers.

Each of the next $j$ lines contains two integers $p_1$ and $p_2$, representing the processing durations (in milliseconds) of a job in phase 1 and phase 2, respectively. Both durations are at least $1$ and will never exceed the number of grams in exactly one metric tonne.

## Output

Print a single line: `JOB i` (where job `i`'s $p_1 + p_2$ exceeds $T$) or `LOAD c` (where phase `c`'s total load exceeds $T$).

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

In Example 1, job 1 requires 70 + 60 = 130 > 100 milliseconds sequentially, so `JOB 1` proves the timeframe is impossible. 
In Example 2, no single job exceeds 150, but phase 1 must process 50+50+50+50 = 200 > 150 milliseconds of work in total, so `LOAD 1` is the rejection certificate.
