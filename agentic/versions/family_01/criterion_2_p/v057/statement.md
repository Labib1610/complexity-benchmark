# Orbital Resonance

Time limit: 1 s
Memory limit: 256 MB

The deployment of a deep space communications network is executed in three mandatory phases. 

Phase I (Orbital Insertion and Hazard Mapping) has just concluded. This initial stage confirmed the active status of $n$ relay satellites, numbered 1 through $n$, and successfully mapped $m$ proximity hazards. Each hazard indicates that a specific pair of satellites is physically drifting too close together.

You are responsible for Phase II (Transmitter Initialization). Each satellite features a dual-band transmitter that must be permanently locked to either operating mode 1 or operating mode 2. If any proximity hazard involves two satellites locked to the exact same mode, a resonance cascade will occur and a system-wide failure will be triggered. You must determine if there is a way to lock the modes for all $n$ satellites such that no hazard involves matching modes.

If Phase II completes successfully, the network advances to Phase III (Telemetry Synchronization). The synchronization protocol requires the full sequence of assigned modes $s_1, s_2, \dots, s_n$ to be fed into the primary diagnostic system. To ensure deterministic diagnostic testing, the system demands that you supply the lexicographically smallest sequence of modes that prevents resonance cascades. If no safe configuration is possible, Phase III is aborted entirely.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of satellites verified in Phase I and the number of mapped proximity hazards.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ — a proximity hazard between satellite $u$ and satellite $v$.

## Output
If it is impossible to pass Phase II without triggering a failure, output a single line containing `NO`.
Otherwise, output `YES` on the first line to authorize Phase III. On the second line, output $n$ integers $s_1, \dots, s_n$ (each being either 1 or 2), representing the mode locked for each satellite from 1 to $n$. This sequence must be the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
