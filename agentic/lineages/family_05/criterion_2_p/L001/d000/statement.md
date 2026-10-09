# Telemetry Calibration Module

Time limit: 2 s   Memory limit: 256 MB

## Description

The automated flight control system operates in three consecutive phases. First, in the hardware registration phase, exactly **k** drones (numbered 1 to **k**) are permanently paired with exactly **k** control stations (numbered 1 to **k**). Each drone is wired to one station, and each station communicates with exactly one drone.

Second, in the telemetry calibration phase, the system must assign each drone exactly one transmission frequency from a pool of **k** available frequencies (numbered 1 to **k**). The system conducts a series of test broadcasts, resulting in a database of stable configurations. Each stable configuration is defined by three parameters: a drone ID, a control station ID, and a frequency ID.

Finally, in the operation phase, the fleet executes its flight plan using the chosen configurations.

Your task is to implement the software for the telemetry calibration phase. You are provided with the database of stable configurations. Because the hardware registration phase has already locked the drone-to-station pairings, you will notice that any given drone only ever appears with its assigned control station in the database, and no control station is assigned to more than one drone.

You must select exactly **k** configurations from the database such that every drone, every control station, and every frequency is utilized exactly once in the final selection. Determine if a complete calibration is possible, and if so, output one valid set of configurations to be passed to the operation phase.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 1200, 0 ≤ **t** ≤ **k** · **k**), representing the number of drones (which is also the number of stations and frequencies) and the number of stable configurations in the database.

Each of the next **t** lines contains three integers **d**, **c**, and **f** (1 ≤ **d**, **c**, **f** ≤ **k**), representing a stable configuration consisting of drone **d**, control station **c**, and frequency **f**. All configurations in the input are distinct. As guaranteed by the registration phase, for any drone **d**, all its configurations will feature the same station **c**, and no two distinct drones will be associated with the same station.

## Output

If a valid selection of **k** configurations can be formed, print `YES` on the first line. Then, print **k** lines, each containing the three integers `d c f` of a chosen configuration. You may print the configurations in any order. If there are multiple valid selections, any of them will be accepted.

If it is impossible to complete the telemetry calibration, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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
