# Problem A — Telemetry Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

The automated workflow of the deep-space observatory *Ozymandias* operates in three sequential phases:

**Phase 1: Signal Acquisition.** The observatory captures raw anomalous energy signatures and partitions them into $j$ independent data streams. This phase is considered instantaneous for the scope of your system; all streams are available at microsecond $0$.

**Phase 2: Quantum Analysis.** The onboard array contains $m$ distinct processors. Each data stream must undergo a predetermined, rigid sequence of analysis steps. The constraints for this phase are strictly enforced by the hardware:
- A stream's analysis steps must be executed in the exact order they are listed. A step cannot begin until the preceding step for that same stream has completely finished.
- Each step must be directed to a specific processor and requires a given number of microseconds to complete.
- Once a processor begins a step, it must run it continuously to completion without interruption.
- A processor can only handle one step at a time. It cannot parallelize multiple steps from the same or different streams.

**Phase 3: Burst Transmission.** The instant that every single data stream has finished its final analysis step, the main antenna initiates a synchronized burst transmission to Earth. 

Your diagnostic module must simulate Phase 2 to coordinate the analysis steps optimally. Calculate the absolute earliest microsecond at which Phase 3 can begin.

## Input

The first line of input contains two integers $j$ and $m$ (1 ≤ $j$ ≤ 10, 1 ≤ $m$ ≤ 10), representing the number of data streams and the number of processors, respectively.

Each of the following $j$ lines describes the analysis sequence for one data stream. A line begins with an integer $o$, the number of analysis steps for that stream. This is followed by $o$ pairs of integers, where each pair specifies the `processor` (1 ≤ `processor` ≤ $m$) and the `duration` in microseconds (1 ≤ `duration` ≤ 1000) for a step. The pairs are listed in the strict chronological order the steps must follow.

The total number of analysis steps across all streams will not exceed 50.

## Output

Print a single integer representing the earliest possible microsecond that Phase 3 can initiate.

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
