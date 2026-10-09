# Problem C — Unmeetable Limit: Prove It

Time limit: 2 s
Memory limit: 256 MB

## Description

A manufacturing plant processes a batch of $j$ components. Each component undergoes exactly two sequential phases: Preparation and Finishing. The operational rules of the plant are as follows:
- A component can only begin its Finishing phase after its Preparation phase is completely finished.
- The Preparation facility can work on at most one component at any given moment.
- The Finishing facility can work on at most one component at any given moment.

For every component, you are provided with the exact duration it requires in the Preparation facility and the duration it requires in the Finishing facility. Management has set a strict deadline $T$, dictating that the entire batch of $j$ components must be completely through both phases by time $T$.

For the given data, it is mathematically impossible to meet the deadline $T$, regardless of how the components are scheduled. Your task is to output a simple certificate that proves the deadline cannot be met.

Based on the operational rules, the impossibility can always be demonstrated by one of the following facts:
- **Individual component bottleneck:** A single component's combined duration for Preparation and Finishing is strictly greater than $T$. Since its phases must occur sequentially, this component alone cannot finish by the deadline. If this is the case, print `JOB i`, where $i$ is the 1-based index of the component.
- **Facility capacity exceeded:** The sum of all durations for a single facility (either Preparation or Finishing) is strictly greater than $T$. Since a facility processes one component at a time, it cannot complete its assigned work by the deadline. If this is the case, print `LOAD c`, where $c$ is 1 if the Preparation facility is overloaded, or 2 if the Finishing facility is overloaded.

The input guarantees that exactly one valid output of this format exists.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the durations of a component in the Preparation facility and the Finishing facility, respectively.

## Output

Print a single line containing the certificate of impossibility: either `JOB i` (where component $i$'s total duration exceeds $T$) or `LOAD c` (where facility $c$'s total load exceeds $T$).

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

In Example 1, component 1 needs $70 + 60 = 130 > 100$ time units sequentially, so `JOB 1` proves the limit is impossible. 
In Example 2, no single component exceeds 150, but the Preparation facility must handle $50+50+50+50 = 200 > 150$ units of work in total, so `LOAD 1` is the evidence.
