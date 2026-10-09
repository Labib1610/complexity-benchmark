# Problem A — Deep Space Sequencing

Time limit: 5 s   Memory limit: 256 MB

## Description

The daily operations of a deep space probe are divided into three phases. In Phase 1, mission control receives observation requests from Earth and translates them into sequences of instrument activations. This phase is handled by a separate subsystem and is already complete. Your task is to implement the module for Phase 2: scheduling these activations on the probe's hardware. Once Phase 2 concludes, Phase 3 begins, during which the probe compresses the gathered data and transmits it back to Earth.

To maximize the probe's time in low-power sleep mode, Phase 2 must finish as early as possible. 

The probe is equipped with **m** distinct scientific instruments. You are given **j** observation sequences. Each sequence consists of a strict progression of activation steps. Each step requires exclusive control of a specific instrument for a designated number of time units. 

The scheduling module must adhere to the following constraints:
- The progression of steps within each sequence must be strictly followed. A step in a sequence can only commence after the immediately preceding step in that same sequence has completely finished.
- Each instrument can execute at most one step at any given moment.
- Once an instrument begins executing a step, it must run continuously until that step's required time is fulfilled (it cannot be interrupted).

Determine the earliest possible time at which Phase 3 can begin. This is exactly the moment the final step of the final sequence in Phase 2 completes.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of observation sequences and the number of instruments on the probe.

Each of the following **j** lines details a single observation sequence. A line begins with an integer **o**, the number of steps in the sequence. This is followed by **o** pairs of integers, where each pair specifies the `instrument` (1 ≤ instrument ≤ m) and the `duration` (1 ≤ duration ≤ 1000) for a step. The pairs are listed in the strict progression order required by the sequence.

The total number of steps across all sequences will not exceed 50.

## Output

Print a single integer: the earliest possible time at which Phase 3 can begin (the minimum time required to complete all observation sequences).

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

In Example 1, two identical observation sequences each require instruments 1, 2, and 3 in order (2 time units each). The second sequence trails the first through the instruments and finishes at time 8. In Example 3, the two sequences use different instruments and run in parallel, finishing at time 4.
