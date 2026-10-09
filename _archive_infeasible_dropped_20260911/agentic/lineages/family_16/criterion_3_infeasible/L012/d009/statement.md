# Spaceship Power Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the chief engineer of a spaceship managing $j$ critical subsystems. Each subsystem requires two distinct energy bursts to reboot: a **Capacitor Charge** burst and a **System Initialization** burst. 

The reboot sequence is strictly governed by the following safety constraints:
1. **Precedence**: For any given subsystem, its System Initialization burst cannot begin until its Capacitor Charge burst has completely finished.
2. **Capacitor Grid Capacity**: The ship's capacitor grid can process at most one Capacitor Charge burst at any given moment.
3. **Initialization Grid Capacity**: The ship's initialization grid can process at most one System Initialization burst at any given moment.
4. **Time Limit**: All bursts across all subsystems must be fully completed within a strict operating window of $T$ milliseconds.

The ship's computer has determined that no valid sequence of operations can satisfy all four constraints simultaneously. To isolate the bottleneck, you must conduct three hypothetical scheduling experiments. The input data guarantees that exactly one of the three experiment types will yield a minimum completion time strictly greater than $T$. You must output the corresponding error code for the experiment that proves $T$ is impossible to meet:

- **Experiment Type 1 (Output `JOB i`)**: Remove the capacity limits of both grids (ignoring Constraints 2 and 3), allowing any number of bursts to run simultaneously. Calculate the earliest possible time all bursts for a specific subsystem $i$ can finish, respecting its precedence rule (Constraint 1). If this minimum time exceeds $T$, output `JOB i` where $i$ is the 1-based index of the subsystem. If multiple subsystems exceed $T$ under this experiment, outputting any such index $i$ is acceptable.
- **Experiment Type 2 (Output `LOAD 1`)**: Set the duration of all System Initialization bursts to 0 milliseconds and remove the initialization grid's capacity limit (ignoring Constraint 3). Calculate the earliest possible time all bursts across all subsystems can finish, respecting the capacitor grid's serial limit (Constraint 2) alongside all precedence rules. If this minimum time exceeds $T$, output `LOAD 1`.
- **Experiment Type 3 (Output `LOAD 2`)**: Set the duration of all Capacitor Charge bursts to 0 milliseconds and remove the capacitor grid's capacity limit (ignoring Constraint 2). Calculate the earliest possible time all bursts across all subsystems can finish, respecting the initialization grid's serial limit (Constraint 3) alongside all precedence rules. If this minimum time exceeds $T$, output `LOAD 2`.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in milliseconds for the subsystem's **Capacitor Charge** burst and its **System Initialization** burst, respectively.

## Output

Print a single line containing either `JOB i` (if Experiment Type 1 yields a minimum time $> T$ for subsystem $i$), `LOAD 1` (if Experiment Type 2 yields a minimum time $> T$), or `LOAD 2` (if Experiment Type 3 yields a minimum time $> T$).

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

In Example 1, under Experiment Type 1 for subsystem 1, we ignore grid capacities. However, subsystem 1 must still complete its 70 ms Capacitor Charge followed immediately by its 60 ms System Initialization. The earliest possible time to complete both is 130 ms. Since 130 ms strictly exceeds the 100 ms Time Limit, `JOB 1` is a valid bottleneck proof.

In Example 2, no individual subsystem exceeds the 150 ms limit under Experiment Type 1. However, under Experiment Type 2, we assume System Initialization bursts take 0 ms. We must still process all four 50 ms Capacitor Charge bursts one at a time due to the capacitor grid's serial limit. The earliest possible time to finish all bursts is 200 ms. Since 200 ms strictly exceeds the 150 ms Time Limit, `LOAD 1` is the valid bottleneck proof.