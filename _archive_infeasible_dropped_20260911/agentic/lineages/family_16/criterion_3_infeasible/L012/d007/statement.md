# Spaceship Power Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the chief engineer of a spaceship managing $j$ critical subsystems. Each subsystem requires two distinct energy bursts to reboot: a **Capacitor Charge** burst and a **System Initialization** burst. 

The reboot sequence is strictly governed by the following safety constraints:
1. **Precedence**: For any given subsystem, its System Initialization burst cannot begin until its Capacitor Charge burst has completely finished.
2. **Capacitor Grid Capacity**: The ship's capacitor grid can process at most one Capacitor Charge burst at any given moment.
3. **Initialization Grid Capacity**: The ship's initialization grid can process at most one System Initialization burst at any given moment.
4. **Time Limit**: All bursts across all subsystems must be fully completed within a strict operating window of $T$ milliseconds.

The ship's computer has determined that no valid sequence of operations can satisfy all four constraints simultaneously. The input data guarantees that exactly one of the following relaxed scenarios still forces an unavoidable violation of Constraint 4. You must isolate the exact bottleneck by outputting the corresponding error code:

- `JOB i` (where $i$ is the 1-based index of a subsystem): It is impossible to satisfy Constraint 4 even if the scheduling problem is reduced to solely processing subsystem $i$ (ignoring the existence of all other subsystems).
- `LOAD 1`: It is impossible to satisfy Constraint 4 even if the scheduling problem is reduced to solely processing the Capacitor Charge bursts of all subsystems (ignoring Constraints 1 and 3).
- `LOAD 2`: It is impossible to satisfy Constraint 4 even if the scheduling problem is reduced to solely processing the System Initialization bursts of all subsystems (ignoring Constraints 1 and 2).

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in milliseconds for the subsystem's **Capacitor Charge** burst and its **System Initialization** burst, respectively.

## Output

Print a single line containing either `JOB i` (if the isolated subsystem $i$ scenario violates the time limit), `LOAD 1` (if the isolated Capacitor Charge scenario violates the time limit), or `LOAD 2` (if the isolated System Initialization scenario violates the time limit).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, if we reduce the problem to solely processing subsystem 1, we must complete its 70 ms Capacitor Charge and its 60 ms System Initialization. Due to Constraint 1 (Precedence), these cannot overlap. The absolute minimum time to complete both is 130 ms. This unavoidably violates the 100 ms Time Limit (Constraint 4). Thus, `JOB 1` is the valid proof.

In Example 2, no individual subsystem exceeds the 150 ms limit. However, if we reduce the problem to solely processing the four Capacitor Charge bursts, Constraint 2 dictates they cannot overlap. The minimum time to process all four 50 ms bursts is 200 ms, which unavoidably violates Constraint 4. Thus, `LOAD 1` is the valid proof.