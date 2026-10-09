# Fleet Docking Assignment

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics center operates a fleet of exactly $q$ delivery drones (assigned serial numbers $1$ through $q$) and exactly $q$ automated landing pads (assigned serial numbers $q+1$ through $2q$).

Due to varying payload weights and firmware versions, a drone cannot land on just any pad. A preliminary telemetry sweep has provided a list of all compatible pairings. A compatible pairing always consists of one drone and one landing pad.

Your software must coordinate the nightly docking sequence. A successful docking sequence requires that every single drone is assigned to exactly one landing pad, and every single landing pad receives exactly one drone. You may only assign drones to pads that are listed as compatible by the telemetry sweep. No drone may be left in the air, no pad may remain empty, and no drone or pad may be involved in more than one assignment.

If a successful docking sequence is possible, you must output the exact assignments to be executed. If the compatible pairings do not permit a full assignment, you must output a specific alert so the drones can be diverted to an alternate facility.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of drones (which equals the number of landing pads) and the total number of compatible pairings from the telemetry sweep.
This is followed by $t$ lines, each containing two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that drone $a$ is compatible with landing pad $b$.

## Output
If the docking sequence can proceed, print `YES` followed by $q$ lines, each containing the two serial numbers of one chosen assignment.
If a full assignment is impossible from the given compatible pairings, print `NO`.

## Example 1
### Input
```text
3 4
1 4
2 4
2 5
3 6
```
### Output
```text
YES
1 4
2 5
3 6
```

## Example 2
### Input
```text
2 2
1 3
2 3
```
### Output
```text
NO
```
