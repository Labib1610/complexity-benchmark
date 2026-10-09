# Problem C — Rift Seal: Denial Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

An arcane guild must complete $j$ magical rituals (logged as **jobs**) to seal a dimensional rift. Each job $i$ requires a continuous channeling duration of $p_{1,i}$ at the Earth Monolith (Focus 1) and a continuous channeling duration of $p_{2,i}$ at the Sky Monolith (Focus 2). 

A valid schedule must assign a start time $x_{1,i}$ at Focus 1 and a start time $x_{2,i}$ at Focus 2 for every job $i$, satisfying the following system of constraints:
- $x_{1,i} \ge 0$ for all $i$.
- $x_{2,i} \ge x_{1,i} + p_{1,i}$ for all $i$ (a job's Sky channeling can only begin after its Earth channeling has fully completed).
- For any two distinct jobs $i$ and $k$, the intervals $[x_{1,i}, x_{1,i} + p_{1,i})$ and $[x_{1,k}, x_{1,k} + p_{1,k})$ must not intersect (Focus 1 processes one job at a time).
- For any two distinct jobs $i$ and $k$, the intervals $[x_{2,i}, x_{2,i} + p_{2,i})$ and $[x_{2,k}, x_{2,k} + p_{2,k})$ must not intersect (Focus 2 processes one job at a time).

The rift will fully open in exactly $T$ seconds, meaning the schedule must also satisfy:
- $x_{2,i} + p_{2,i} \le T$ for all $i$.

The number of valid interval arrangements is extraordinarily large, as the processing order on Focus 1 need not match the order on Focus 2, and arbitrary idle times may be inserted between jobs. However, for all test cases provided in this problem, it is guaranteed that the system of constraints has no valid solution. 

Your task is not to exhaustively evaluate the permutation space to confirm this, but to output a short Denial Certificate that directly proves the time limit $T$ is impossible. The guild recognizes two types of Denial Certificates. Exactly one of the following two reasons will always apply to any given input:

- **Single-Job Sequence Violation:** There exists a job whose own sequential constraints imply $x_{2,i} + p_{2,i} > T$ even if it were the only job in the system. That is, $p_{1,i} + p_{2,i} > T$.
  Print: `JOB i` — where $i$ (1-based) is the index of such a job.

- **Monolith Capacity Violation:** The non-intersection constraints on a single Focus mandate that its total active time cannot exceed the available window $[0, T]$. If the sum of $p_{1,i}$ over all jobs exceeds $T$, or the sum of $p_{2,i}$ over all jobs exceeds $T$, that Focus is mathematically overloaded.
  Print: `LOAD c` — where $c$ is 1 if Focus 1 is overloaded, or 2 if Focus 2 is overloaded.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_{1,i}$ and $p_{2,i}$ ($1 \le p_{1,i}, p_{2,i} \le 1000000$): the channeling times of job $i$ at Focus 1 and Focus 2 respectively.

## Output

Print a single line: `JOB i` (for a job whose $p_{1,i} + p_{2,i}$ exceeds $T$) or `LOAD c` (for a Focus $c$ whose total required processing time exceeds $T$).

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

In Example 1, the sequential constraints for job 1 dictate that $x_{2,1} + p_{2,1} \ge x_{1,1} + p_{1,1} + p_{2,1} \ge 0 + 70 + 60 = 130$. Since $130 > 100$, `JOB 1` is the correct certificate.
In Example 2, no single job violates the sequence constraint, but the non-intersection constraints on Focus 1 require at least $50+50+50+50 = 200$ seconds of active time. Since $200 > 150$, the capacity of Focus 1 is mathematically violated, making `LOAD 1` the certificate.
