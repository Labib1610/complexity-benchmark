# Problem B — Visual Effects Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

A studio must schedule the rendering of **j** visual effects. To do this, you must select a single schedule, defined as a permutation $\pi$ of the **j** effects. There are **j**! possible orderings to consider.

The studio operates a rendering pipeline on dedicated hardware. In this specific workload, exactly two processing nodes are active sequentially: a geometry solver and a light tracer. Every effect must be processed first on the solver, and then on the tracer.

To evaluate a given schedule $\pi$, the pipeline execution follows these mechanical rules:
- Both the geometry solver and the light tracer process the effects in the exact sequence given by $\pi$.
- A processing node can only handle one effect at a time, running it to completion without interruption.
- Each effect begins on the geometry solver as early as possible (the first effect in $\pi$ starts at time 0, and each subsequent effect starts exactly when the previous one finishes on the solver).
- Each effect begins on the light tracer as early as possible. Specifically, an effect starts on the tracer at the exact moment it finishes on the solver, unless the tracer is still busy with the previous effect in $\pi$, in which case it must wait until the tracer becomes idle.

Your task is to determine the minimum possible global completion time across all **j**! possible permutations. The global completion time is the exact moment the final effect in $\pi$ finishes on the light tracer. 

## Input

The first line provides a single integer **j** (1 ≤ j ≤ 200000), representing the number of visual effects.
Each of the subsequent **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000). These represent the required processing time for an effect on the geometry solver and the light tracer, respectively.

## Output

Print a single integer representing the absolute minimum time at which all effects can be completely finished.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single effect takes 5 on the solver then 3 on the tracer, finishing at time 8.
