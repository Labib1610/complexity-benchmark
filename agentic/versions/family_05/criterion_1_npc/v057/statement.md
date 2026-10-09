# Phase 2: Resource Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description

The automated data pipeline of a deep-space control node follows a strict three-phase sequence to transmit telemetry.

**Phase 1: Bootstrapping and Hardware Diagnostics.** The node powers up its communication hardware, consisting of **k** uplink dishes, **k** cryptographic keys, and **k** memory buffers. Each hardware type has its units numbered from 1 to **k**. The system runs a diagnostic sweep to test component compatibility, producing a log of viable configurations. A viable configuration is a specific triad `(dish, key, buffer)` that operates without signal degradation.

**Phase 2: Resource Allocation (Your Task).** The allocation firmware must parse the log from Phase 1. It must extract exactly **k** configurations from the log such that every uplink dish, every cryptographic key, and every memory buffer is assigned to exactly one of the chosen configurations.

**Phase 3: Transmission.** If Phase 2 successfully finds the required configurations, the node locks them in and initiates the telemetry download. If Phase 2 determines no such allocation is possible, it must issue an abort signal to prevent data corruption.

You are responsible solely for the Phase 2 Resource Allocation module. Given the diagnostic log from Phase 1, determine if it is possible to proceed to Phase 3, and if so, output the configurations to be locked in.

## Input

The first line of the log contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of units of each hardware type, and the total number of viable configurations found during Phase 1.
Each of the next **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a viable configuration consisting of uplink dish **x**, cryptographic key **y**, and memory buffer **z**. No configuration appears more than once in the log.

## Output

If a valid allocation of **k** configurations exists to allow Phase 3 to begin, print `YES` on the first line, followed by **k** lines, each containing the three integers `x y z` of one selected configuration. Any valid allocation where every dish, key, and buffer is used exactly once is acceptable. The configurations may be printed in any order.

If no valid allocation exists, print `NO` (which serves as the Phase 3 abort signal).

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both viable configurations in the log use cryptographic key 1, so cryptographic key 2 can never be assigned to a configuration.
