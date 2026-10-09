# Problem C — Pipeline Admission Controller

Time limit: 2 s   Memory limit: 256 MB

## Description

You are implementing Phase 2 of a distributed task management system. The full pipeline consists of:
1. **Ingestion**: Receiving user requests and parsing them.
2. **Admission Control (Your Task)**: Quickly rejecting batches that are mathematically impossible to complete within the user's requested time window.
3. **Scheduling**: Finding the optimal execution order for accepted batches.
4. **Dispatch**: Sending the ordered instructions to the hardware.

You are responsible only for Phase 2. The pipeline routes a batch of **j** jobs to your module along with a maximum time window **T**. Each job requires a certain amount of time on Processor 1, and subsequently a certain amount of time on Processor 2. A job cannot begin on Processor 2 until it has completely finished on Processor 1. Processor 1 and Processor 2 each handle only one job at a time.

Every batch routed to your module in this environment has already been flagged as impossible to complete within **T**. Your program must not search for a schedule; its sole function is to generate a short rejection certificate that the Ingestion module can return to the user.

Exactly one of the following two reasons always applies for the provided inputs. Print the certificate for the one that holds:

- **Sequential bottleneck**: A single job is too long. If some job's required time on Processor 1 and Processor 2 add up to more than **T**, that job alone cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based index) is such a job.

- **Processor saturation**: A processor is overloaded. A processor handles jobs one at a time, so it needs at least the sum of all its required times. If the total work on Processor 1 (or Processor 2) exceeds **T**, the window is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total required time on Processor **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200,000, 1 ≤ T ≤ 1,000,000,000).
The next **j** lines each contain two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1,000,000): the required time for the job on Processor 1 and Processor 2, respectively.

## Output

Print a single line containing the certificate: either `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a processor c whose total load exceeds T).

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

In Example 1, job 1 requires 70 + 60 = 130 > 100 time units in sequence, making the window impossible. Thus, `JOB 1` is the correct certificate. 
In Example 2, no single job's combined time exceeds 150, but Processor 1 must perform 50 + 50 + 50 + 50 = 200 > 150 units of work in total. Since it processes sequentially, `LOAD 1` is the correct certificate.
