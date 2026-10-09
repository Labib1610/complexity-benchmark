# Problem A — Pipeline Throughput Optimization

Time limit: 5 s   Memory limit: 256 MB

## Description

A research institute is evaluating a batch of **j** proposals using a panel of **m** domain experts. The evaluation of each proposal is structured as a streamlined pipeline of stages. Each stage dictates the specific expert required and the exact duration (in hours) the evaluation takes.

The evaluation flow operates under three highly regular mechanics:
- **Linear Progression:** Each proposal advances through its stages in the exact sequence provided. A stage can only enter an expert's queue once the preceding stage for that proposal's pipeline has completely finished.
- **Dedicated Processing:** An expert handles exactly one stage of one proposal at any given moment.
- **Continuous Execution:** Once an expert begins a stage, they process it continuously for its full duration, without any pauses.

The system functions as a network of intersecting pipelines. As proposals move from one expert to the next, experts independently process the stages assigned to them. By optimally ordering the stages within each expert's workload, the institute can maximize its overall throughput. 

Assume all pipelines activate at hour 0. Determine the minimum total number of hours required from the start until the final stage of the last remaining proposal is completely finished.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of proposals and the number of experts.
Each of the subsequent **j** lines describes the pipeline for one proposal. A line starts with an integer **o** (the number of stages), followed by **o** pairs of integers `expert` and `duration` (1 ≤ expert ≤ m, 1 ≤ duration ≤ 1000). These pairs define the proposal's stages in their strict sequential order.
The total number of stages across all proposals is at most 50.

## Output

Output a single integer: the minimum total hours needed to completely finish all proposals.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical proposals each require expert 1, then expert 2, then expert 3 (each stage taking 2 hours). The second proposal can trail the first through the pipeline, allowing both to be completely processed by hour 8. In Example 3, the two proposals require different experts and flow through the system simultaneously, finishing at hour 4.
