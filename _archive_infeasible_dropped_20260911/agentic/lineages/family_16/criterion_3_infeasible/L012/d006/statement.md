# Spaceship Power Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the chief engineer of a spaceship managing $j$ critical subsystems. Each subsystem requires two power bursts to reboot: a **Capacitor Charge** burst and a **System Initialization** burst. 

The reboot sequence is subject to the following safety constraints:
1. **Precedence**: For any given subsystem, its System Initialization burst must start at or after the exact moment its Capacitor Charge burst finishes.
2. **Capacitor Grid Capacity**: The ship's capacitor grid can only handle one Capacitor Charge burst at a time. No two Capacitor Charge bursts may overlap.
3. **Initialization Grid Capacity**: The ship's initialization grid can only handle one System Initialization burst at a time. No two System Initialization bursts may overlap.
4. **Time Limit**: The entire reboot process for all bursts across all subsystems must be completely contained within a strict operating window of $[0, T]$ milliseconds.

The ship's computer has determined that the window $T$ is too short to reboot all subsystems. The input data guarantees that exactly one of the following theoretical minimum time bounds strictly exceeds $T$, which isolates the exact bottleneck. You must output the corresponding error code:

- `JOB i` (where $i$ is the 1-based index of a subsystem): The minimum time required to process subsystem $i$'s Capacitor Charge and System Initialization sequentially strictly exceeds $T$.
- `LOAD 1`: The minimum time required to process all $j$ Capacitor Charge bursts on the capacitor grid, assuming they are processed back-to-back with zero idle time, strictly exceeds $T$.
- `LOAD 2`: The minimum time required to process all $j$ System Initialization bursts on the initialization grid, assuming they are processed back-to-back with zero idle time, strictly exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in milliseconds for the subsystem's **Capacitor Charge** burst and its **System Initialization** burst, respectively.

## Output

Print a single line containing either `JOB i` (if subsystem $i$'s sequential duration exceeds $T$), `LOAD 1` (if the back-to-back Capacitor Charge duration exceeds $T$), or `LOAD 2` (if the back-to-back System Initialization duration exceeds $T$).

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

In Example 1, the first subsystem requires 70 milliseconds for its Capacitor Charge and 60 milliseconds for its System Initialization. Processed sequentially, this requires $70 + 60 = 130$ milliseconds, which strictly exceeds the window $T = 100$. This makes `JOB 1` the valid proof of impossibility. 

In Example 2, no individual subsystem exceeds $T = 150$. However, the Capacitor Grid must process four bursts of 50 milliseconds each. Processed back-to-back, these require $50 + 50 + 50 + 50 = 200$ milliseconds, which strictly exceeds $T = 150$, making `LOAD 1` the valid proof.