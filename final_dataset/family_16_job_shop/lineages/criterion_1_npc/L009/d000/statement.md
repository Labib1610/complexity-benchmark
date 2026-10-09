# Problem A — Proposal Evaluation

Time limit: 5 s   Memory limit: 256 MB

## Description

Consider a batch of **j** research proposals that must be evaluated by a panel of **m** domain experts. Every proposal mandates a specific sequence of review stages. Each stage is defined by the specific expert required to conduct it and the exact number of hours it consumes.

The evaluation process is governed by three strict protocols:
- **Sequential Dependence:** The stages of any single proposal must be executed in the exact order they are listed. A stage may only commence after the immediately preceding stage for that same proposal has entirely concluded.
- **Expert Focus:** An expert cannot divide their attention; they may only conduct one stage of one proposal at any given moment.
- **Uninterrupted Work:** Once an expert begins a stage, they must dedicate themselves to it continuously until the required hours have elapsed, with no pauses or interruptions.

All evaluations begin at hour 0. Given these protocols, you must organize the timeline for every stage. Find the minimum total number of hours required from the start of the process until the final stage of the final proposal is completely finished.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one research proposal: an integer **o** (the number of stages) followed by **o** pairs of integers `expert duration` (1 ≤ expert ≤ m, 1 ≤ duration ≤ 1000), listing the proposal's review stages in their strict sequential order.
The total number of stages across all proposals is at most 50.

## Output

Print a single integer: the minimum total number of hours required to finish all proposals.

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

In Example 1, two identical proposals each require expert 1, then expert 2, then expert 3 (each stage taking 2 hours). The second proposal can trail the first through the experts, allowing both to be completely reviewed by hour 8. In Example 3 the two proposals require different experts and can be reviewed simultaneously, finishing at hour 4.
