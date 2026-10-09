# Problem B — Core Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description

A batch of **j** energy cores must be calibrated. Calibration involves two sequential stages for every core: excitation followed by dampening. For each core, you are given the exact time it takes to be excited, and the exact time it takes to be dampened.

The calibration facility operates under the following rules:

- The exciter can process only one core at a time.
- The dampener can process only one core at a time.
- A core can begin dampening only after its excitation is completely finished.
- Cores are placed on a fixed track. You may choose the order of the cores on the track, but this single order dictates the sequence they enter the exciter, and subsequently, the sequence they enter the dampener.
- If a core finishes excitation but the dampener is still processing an earlier core, the new core waits safely in a queue between the two devices.
- Neither device will sit idle if a core is ready and waiting for it.

Choose the initial sequence of the cores to minimize the time at which the **last** core finishes dampening. Report that earliest possible finish time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of a core in the exciter and the dampener, respectively.

## Output

Print a single integer: the smallest possible time at which all cores have finished dampening.

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

In Example 2, the single core takes 5 in the exciter and then 3 in the dampener, finishing at time 8.
