# Problem A — Quantum Calibration Alignment

Time limit: 5 s
Memory limit: 256 MB

## Description

You are configuring a quantum array equipped with $m$ distinct microwave emitters. The configuration process requires executing $j$ independent entanglement sequences.

Each sequence is defined as a strict progression of calibration phases. Every phase dictates that a specific emitter must be activated for an exact number of nanoseconds. 

The system operates under the following mechanical constraints:
- The phases within a single entanglement sequence must be executed in the exact order they are given. A phase within a sequence can only commence after the preceding phase in that same sequence has completely finished.
- An emitter can only handle one phase at a time. Once an emitter begins a phase, it remains locked and must run continuously until that phase's required duration has elapsed.
- Different emitters are completely independent and can be active at the same time.

Your objective is to determine the minimum number of nanoseconds required from the start until all phases across all sequences are completely finished. 

## Input

The first line contains two integers $j$ and $m$ (1 ≤ $j$ ≤ 10, 1 ≤ $m$ ≤ 10), representing the number of entanglement sequences and the number of emitters, respectively.

Each of the subsequent $j$ lines details one entanglement sequence. The line starts with an integer $o$, representing the number of phases in the sequence. Following this are $o$ pairs of integers, each formatted as `emitter_id duration` (1 ≤ `emitter_id` ≤ $m$, 1 ≤ `duration` ≤ 1000). These pairs list the phases in the strict chronological order they must follow.

The total number of phases across all $j$ sequences is guaranteed to be at most 50.

## Output

Output a single integer: the minimum number of nanoseconds required to complete all sequences.

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

In Example 1, two identical sequences each mandate phases on emitters 1, 2, and 3 (each requiring 2 nanoseconds). The second sequence can trail the first through the emitters, allowing everything to conclude at 8 nanoseconds. 

In Example 3, the two sequences rely on entirely different emitters and can progress simultaneously without interference, finishing in the maximum of their individual durations (4 nanoseconds).
