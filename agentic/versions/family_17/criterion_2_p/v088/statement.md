# Problem B — Diagnostic to Synthesis Pipeline

Time limit: 2 s   Memory limit: 256 MB

## Description
The initialization of a dual-layer signal processor operates in a strict three-phase pipeline: diagnostic scanning, bridge synthesis, and final calibration. You are responsible for implementing the second phase.

Phase 1 (Diagnostic Scanning) has already been completed by the hardware. It evaluated the processor's $2q$ hardware terminals, where terminals $1$ through $q$ are primary-layer transmitters and terminals $q+1$ through $2q$ are secondary-layer receivers. This scan produced a manifest of $t$ viable interference-free channels, each capable of linking one specific transmitter to one specific receiver.

Phase 2 (Bridge Synthesis) is your task. You must process the Phase 1 manifest to select exactly $q$ independent signal bridges. For Phase 3 to begin, your selection must incorporate every single terminal (all $q$ transmitters and all $q$ receivers) into exactly one bridge. A terminal cannot be left out, nor can it be assigned to multiple bridges.

Phase 3 (Final Calibration) will automatically tune the processor based on your output, provided a valid synthesis is found. If no valid synthesis exists, the pipeline must be aborted.

Evaluate the Phase 1 manifest and determine if Phase 2 can be successfully completed.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000) — the number of terminals on each layer and the number of viable channels found during Phase 1.
The following $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a viable channel from the manifest between transmitter $a$ and receiver $b$.

## Output
If Phase 2 can be completed, print `YES` on the first line, followed by $q$ lines detailing the chosen channels (each line containing the two terminal IDs of the bridge). If it is impossible to incorporate every terminal, print `NO`.

## Example 1

### Input
```
3 4
1 4
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

## Example 2

### Input
```
2 2
1 3
2 3
```

### Output
```
NO
```
