# Calibration Cycle Alignment

Time limit: 2 s   Memory limit: 256 MB

## Description
An observatory tracks a fleet of $q$ observation satellites, identified by integer codes from 1 to $q$. It also monitors an equal number of designated target sectors in the sky, identified by integer codes from $q+1$ to $2q$.

During a calibration cycle, a satellite can be focused on a target sector. However, due to orbital mechanics and sensor constraints, a specific satellite can only focus on a specific target sector if their relative alignment is listed in the day's telemetry manifest. The manifest contains a list of viable focus pairings, each specifying one satellite and one target sector. A satellite may have viable pairings with multiple sectors, and a sector may be viable for multiple satellites. The manifest is exhaustive; no unlisted pairings may be used.

A calibration routine consists of selecting a subset of these viable pairings to activate. When a pairing is activated, the involved satellite is committed to the involved sector for the duration of the cycle. A committed satellite cannot be assigned to any other sector, and a committed sector cannot be assigned to any other satellite.

The administration requires a complete calibration cycle where absolutely no resources are left idle. You must determine whether it is possible to activate a set of pairings from the manifest such that every single satellite and every single target sector is committed exactly once. If this is achievable, provide the list of pairings to activate; otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000).
The next $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a viable pairing between satellite $a$ and target sector $b$.

## Output
If a complete calibration cycle is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of an activated pairing. If it is impossible, print `NO`.

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
