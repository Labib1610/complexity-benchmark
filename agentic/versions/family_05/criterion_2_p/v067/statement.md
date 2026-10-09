# Telemetry Calibration Module

Time limit: 2 s   Memory limit: 256 MB

## Description

The automated flight control system maintains a database of stable communication configurations. Each configuration is defined by a triplet of parameters: a drone ID, a control station ID, and a frequency ID.

Before this database is generated, the system undergoes a hardware registration phase. During this phase, exactly **k** drones (numbered 1 to **k**) are permanently wired to exactly **k** control stations (numbered 1 to **k**). Each drone connects to a single station, and each station is reserved for a single drone. 

Because of this physical lock-in, the stable configurations exhibit a strict structural property. If you examine all configurations involving a particular drone, they will all feature the identical control station. Similarly, it is guaranteed that no two distinct drones will ever be listed alongside the same control station anywhere in the database. 

The system has a pool of exactly **k** available frequencies (numbered 1 to **k**). The database contains a total of **t** stable configurations that have passed preliminary test broadcasts. 

Your task is to implement the software for the final telemetry calibration phase. You must filter the database to select exactly **k** configurations to be passed to the operation phase. This selection must satisfy a strict requirement: every drone, every control station, and every frequency must be utilized exactly once in the final set of configurations. Determine whether it is possible to form such a complete calibration, and if it is, output one valid set.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 1200, 0 ≤ **t** ≤ **k** · **k**), representing the number of drones, stations, and frequencies, as well as the total number of stable configurations.

Each of the following **t** lines contains three integers **d**, **c**, and **f** (1 ≤ **d**, **c**, **f** ≤ **k**), which describe a stable configuration consisting of drone **d**, control station **c**, and frequency **f**. All configurations provided in the input are distinct. As established during hardware registration, any given drone **d** will only appear with one specific station **c**, and no station will be associated with more than one drone.

## Output

If a valid subset of **k** configurations can be formed, print `YES` on the first line. Then, output **k** lines, each containing the three integers `d c f` of a selected configuration. You may output these configurations in any order. If multiple valid subsets exist, any of them will be accepted.

If no such complete calibration is possible, print `NO`.

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
