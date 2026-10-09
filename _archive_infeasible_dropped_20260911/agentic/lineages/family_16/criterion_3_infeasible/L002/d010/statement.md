# Infeasible Production Schedule

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a production schedule for $j$ manufacturing jobs. The factory operates for a single continuous shift of exactly $T$ minutes.

Each job $i$ (from $1$ to $j$) requires $q_{1,i}$ minutes of continuous processing on the Milling machine, and $q_{2,i}$ minutes of continuous processing on the Polishing machine. 

A valid schedule assigns exactly two active time intervals to each job $i$ (one for Milling of length $q_{1,i}$, and one for Polishing of length $q_{2,i}$) such that the following three requirements are met:
1. **Sequencing:** For every job $i$, its Polishing interval cannot begin until its Milling interval has completely finished.
2. **Capacity:** No two Milling intervals across all jobs may overlap. Similarly, no two Polishing intervals may overlap.
3. **Timeframe:** Every assigned interval must be entirely contained within the shift window from minute $0$ to minute $T$.

For every test case, it is guaranteed that no valid schedule exists that can accommodate all $j$ jobs. Your task is to provide a directly checkable certificate of impossibility by identifying a specific relaxed set of requirements that is already impossible to satisfy on its own.

You must output a valid certificate of impossibility from one of the two forms below. If multiple certificates are valid, you may print any one of them.

- `JOB i` : For the 1-based index $i$, it is impossible to assign the two intervals for job $i$ such that the Sequencing and Timeframe requirements are satisfied, even if we ignore the Capacity requirement and all other jobs.
- `LOAD c` : For stage $c$ (where $c=1$ is Milling, $c=2$ is Polishing), it is impossible to assign the $j$ intervals for this stage such that the Capacity and Timeframe requirements are satisfied, even if we ignore the Sequencing requirement and the other stage.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **q1** and **q2** (1 ≤ q1, q2 ≤ 1000000): the processing times $q_{1,i}$ and $q_{2,i}$ for the $i$-th job.

## Output

Print a single line containing a valid certificate: `JOB i` or `LOAD c` as described above.

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

In Example 1, for job 1, the `JOB` certificate considers only the Sequencing and Timeframe requirements. Job 1 requires a 70-minute Milling interval and a 60-minute Polishing interval. Sequencing dictates that the 60-minute interval must follow the 70-minute interval, requiring at least 130 minutes of total time. The Timeframe requirement restricts all intervals to a 100-minute shift. It is impossible to fit 130 minutes of sequential processing within a 100-minute window, making `JOB 1` a valid certificate.

In Example 2, no single job violates the `JOB` requirements. However, for `LOAD 1`, we consider only the Capacity and Timeframe requirements for the Milling stage. The four jobs require Milling intervals of 50 minutes each. The Capacity requirement dictates that these four intervals cannot overlap, meaning they require a total of 200 minutes of machine time. The Timeframe requirement restricts all intervals to the 150-minute shift. It is impossible to pack 200 minutes of non-overlapping intervals into a 150-minute window, making `LOAD 1` a valid certificate.