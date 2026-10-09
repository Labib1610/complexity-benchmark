# Spaceship Power Allocation Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the chief engineer of a spaceship managing $j$ critical subsystems. Each subsystem requires two power bursts to reboot: a **System Initialization** burst and a **Capacitor Charge** burst. 

The reboot sequence is subject to the following safety constraints:
1. **Precedence**: For any given subsystem, its System Initialization burst must start at or after the moment its Capacitor Charge burst finishes.
2. **Capacitor Grid Capacity**: The ship's capacitor grid can only handle one Capacitor Charge burst at a time across all subsystems.
3. **Initialization Grid Capacity**: The ship's initialization grid can only handle one System Initialization burst at a time across all subsystems.
4. **Time Limit**: The entire reboot process for all subsystems must be completely contained within a strict operating window of $[0, T]$ milliseconds.

The ship's computer has determined that the window $T$ is too short to reboot all subsystems, no matter how they are scheduled. Exactly one of the following error codes will correctly explain the bottleneck:

- `JOB i` (where $i$ is the 1-based index of a subsystem): This code applies if the relaxed system consisting solely of **Precedence** for subsystem $i$ and **Time Limit** for subsystem $i$'s two bursts is logically unsatisfiable on its own.
- `LOAD 1`: This code applies if the relaxed system consisting solely of **Capacitor Grid Capacity** and **Time Limit** for all $j$ Capacitor Charge bursts is logically unsatisfiable on its own.
- `LOAD 2`: This code applies if the relaxed system consisting solely of **Initialization Grid Capacity** and **Time Limit** for all $j$ System Initialization bursts is logically unsatisfiable on its own.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in milliseconds for the subsystem's **Capacitor Charge** burst and its **System Initialization** burst, respectively.

## Output

Print a single line containing either `JOB i` (if subsystem $i$'s constraint subset alone is unsatisfiable), `LOAD 1` (if the Capacitor Grid's constraint subset alone is unsatisfiable), or `LOAD 2` (if the Initialization Grid's constraint subset alone is unsatisfiable).

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

In Example 1, the first subsystem requires 70 milliseconds for its Capacitor Charge and then 60 milliseconds for its System Initialization. The subset of constraints for subsystem 1 requires mapping a 70-ms interval and a subsequent 60-ms interval into the domain $[0, 100]$, which is logically unsatisfiable. This makes `JOB 1` a valid proof of impossibility. 

In Example 2, no individual subsystem's isolated constraints are unsatisfiable. However, the Capacitor Grid is assigned four tasks of 50 milliseconds each. The subset of constraints for the Capacitor Grid requires packing four disjoint 50-ms intervals into the domain $[0, 150]$, which is logically unsatisfiable, making `LOAD 1` the valid proof.