# Orbital Calibration Sequence

Time limit: 1 s   Memory limit: 256 MB

## Description

You are the operations director of the Aethelgard Orbital Station, tasked with calibrating a fleet of **j** autonomous deep-space probes. Every probe requires two sequential calibration phases: Sensor Alignment and Telemetry Sync.

The station is equipped with a single Alignment Bay and a single Sync Bay. The two bays operate independently and can work on different probes simultaneously. The operational protocols are strict:

- A single manifest (an ordered list of all probes) must be generated. Both the Alignment Bay and the Sync Bay will process the probes in the exact sequence specified by this manifest.
- The Alignment Bay handles only one probe at a time.
- The Sync Bay handles only one probe at a time.
- A probe can only begin its Telemetry Sync once its Sensor Alignment is completely finished. If the Sync Bay is busy, the probe must wait; if the Sync Bay is free but the probe's Alignment is not yet done, the Sync Bay remains idle.
- To prevent structural stress on the station's grid, you are guaranteed that the sum of all Sensor Alignment durations across the entire fleet will not exceed $200,000,000,000$ microseconds. 
- Due to docking limitations, the total number of probes is guaranteed to strictly remain under $200,001$.

Your objective is to arrange the manifest so that the time at which the final probe completes its Telemetry Sync is minimized. The station begins processing the first probe on the manifest at time 0.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), representing the number of probes.
Each of the next **j** lines contains two integers, **A** and **B** (1 ≤ A, B ≤ 1000000): the duration of the Sensor Alignment and the duration of the Telemetry Sync for that probe, respectively, in microseconds.

## Output

Print a single integer: the earliest possible time (in microseconds) at which all probes have successfully finished both calibration phases.

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
