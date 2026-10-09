# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A software company manages a continuous integration pipeline for $j$ independent update components. The infrastructure consists of exactly two dedicated machines: a primary compiler and a secondary verifier. 

The pipeline is governed by the following operational rules:
- Every component must first be processed by the primary compiler.
- Only after a component has completely finished its compilation phase can it be transferred to the secondary verifier.
- Each machine is capable of handling at most one component at any given time, with no parallel processing.
- The release manager has allocated a strict time allowance of exactly $T$ minutes. All components must be fully processed through both machines by the end of this allowance.

Due to misconfiguration, the provided parameters in every scenario are flawed. It is guaranteed that all components cannot clear both machines within $T$ minutes, regardless of the scheduling order. 

Your task is not to find a valid schedule, but rather to automatically flag these batches by providing a short diagnostic code demonstrating why the time allowance is mathematically insufficient. The input data guarantees that exactly one of the following diagnostic conditions will be met. Output the corresponding code:

- **Component bottleneck:** A single component requires more time in total (compilation plus verification) than the entire allowance, making it impossible to finish even if it were the only component in the pipeline. Output `JOB i`, where $i$ is the 1-based index of this component.
- **Machine overload:** Because each machine operates sequentially, the total time required by all components on a single machine cannot exceed the allowance. If the primary compiler's total required time exceeds $T$, or if the secondary verifier's total required time exceeds $T$, output `LOAD c`, where $c$ is 1 for the compiler and 2 for the verifier.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$), representing the compilation time and verification time of a component, respectively.

## Output

Output a single line containing either `JOB i` (where component $i$'s combined time exceeds $T$) or `LOAD c` (where machine $c$'s total load exceeds $T$, with $c=1$ for the compiler and $c=2$ for the verifier).

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

In Example 1, component 1 requires 70 + 60 = 130 > 100 minutes sequentially, so `JOB 1` proves the allowance is insufficient. In Example 2, no single component exceeds 150 minutes, but the primary compiler must process 50+50+50+50 = 200 > 150 minutes of work sequentially, so `LOAD 1` is the correct output.
