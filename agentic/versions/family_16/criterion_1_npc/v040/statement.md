# Problem A — Fabrication Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
A custom fabrication facility receives daily batches of bespoke workpieces. Before a batch can be moved downstream to the final packaging and shipping facility, every workpiece in the batch must undergo a specific sequence of treatments. 

The facility contains $m$ distinct treatment bays. You are given a batch of $j$ workpieces. For each workpiece, the required treatments are listed in a strict sequence. Each step in a workpiece's sequence specifies which bay must be used and exactly how many minutes the treatment will take.

To coordinate the floor, you must determine the timing for all treatments subject to the physical constraints of the facility:
- A workpiece must complete its current treatment step fully before it can begin its next step.
- A treatment bay can only accommodate one workpiece at a time.
- Once a workpiece begins a treatment step in a bay, it remains there without interruption until the specified minutes have elapsed.

All workpieces are available at minute 0. The packaging team cannot begin their work until the very last treatment step across all workpieces is entirely finished. Determine the earliest possible minute the packaging team can start.

## Input
The first line contains two integers $j$ and $m$ (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of workpieces and the number of treatment bays, respectively.

Each of the following $j$ lines describes the sequence for one workpiece. A line begins with an integer $o$, the number of treatment steps for this workpiece. This is followed by $o$ pairs of integers. Each pair consists of a `bay_identifier` (1 ≤ bay_identifier ≤ m) and a `duration` (1 ≤ duration ≤ 1000), indicating the bay required and the minutes the step takes. The steps are listed in the exact order they must be performed.

The total number of treatment steps across all workpieces in the batch is at most 50.

## Output
Print a single integer: the earliest minute at which all workpieces have completed all their required treatment steps.

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
In Example 1, two identical workpieces each require bay 1, then bay 2, then bay 3 (taking 2 minutes in each). The second workpiece can follow the first one through the sequence, finishing its final step at minute 8. In Example 3, the two workpieces require different bays and can be processed simultaneously, allowing packaging to begin at minute 4.
