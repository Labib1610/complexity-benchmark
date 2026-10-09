# Problem B — Nightly Railcar Relocation

Time limit: 2 s   Memory limit: 256 MB

## Description
The regional transit system consists of a set of stations linked by one-way tracks. Nightly operations require assigning an integer number of railcars to travel across each track. Due to strict signaling protocols, every track has a hard ceiling on the number of railcars it can safely process per night; an assigned number can be as low as zero but must never exceed this ceiling. 

Additionally, the system enforces a strict balance rule at almost all locations to prevent congestion. For any given station, the sum of railcars arriving via incoming tracks must be identical to the sum of railcars departing via outgoing tracks. There are exactly two stations exempt from this balance rule: a designated central depot and a maintenance yard. Variables such as transit durations, physical track lengths, and the exact sequence of departures are managed by a secondary system and do not constrain these assignments.

Tonight, the transit authority has a precise operational mandate. They must determine if there exists a valid assignment of railcars to tracks—adhering to all ceilings and balance rules—such that the net departure (total departing minus total arriving) at the central depot is exactly equal to a requested target quantity. As a consequence of the balance rules, this exact same quantity will be the net arrival at the maintenance yard. You must generate a valid track assignment that achieves this target quantity, or determine that it cannot be done.

## Input
Line 1: `n` (the number of stations), `m` (the number of tracks), and the constant `1`.
Next line: `s` (the ID of the central depot), `t` (the ID of the maintenance yard), and `d` (the target quantity of railcars).
Next `m` lines: `u`, `v`, and `cap`, representing a one-way track from station `u` to station `v` with a signaling ceiling of `cap` railcars. Stations are identified by integers from 1 to `n`.

## Output
If an assignment meeting all conditions is possible, output `YES` on the first line. On the second line, output `m` space-separated integers representing the number of railcars assigned to each track, in the exact order the tracks were provided in the input. If multiple valid assignments exist, any matching the criteria will be accepted. If no such assignment is possible, output `NO`.

## Example
### Input
```text
4 5 1
1 4 3
1 2 2
1 3 2
2 4 1
3 4 2
2 3 1
```
### Output
```text
YES
1 2 1 2 0
```
