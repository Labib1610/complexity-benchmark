# Problem B — Nightly Railcar Relocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A regional transit authority must deploy replacement railcars across a directed network of stations joined by one-way tracks. Each track carries a strict limit on the number of railcars it can safely accommodate per night, reflecting signaling constraints that cannot be bypassed. A specific total number of replacement railcars must be relocated from a single central depot to a single maintenance yard during a single night.

On every track, the number of railcars scheduled must be a non-negative integer that does not exceed the track's limit. At every station other than the depot and the yard, the railcar count is conserved: the number of arriving railcars must exactly equal the number of departing railcars, ensuring no cars are stranded or duplicated. At the depot, the net departure must equal the required total, and at the yard, the net arrival must equal this total. Other operational details—such as transit times, track lengths, and the exact sequence of departures—are handled by a separate system and must be ignored; only the track limits, station conservation, and the total required relocation size restrict the schedule.

Generate a schedule that relocates the required number of railcars from the depot to the yard without violating any track limits, or state that this total cannot be moved in one night.

## Input
Line 1: `n` (number of stations), `m` (number of tracks), and the constant `1`.
Next line: `s` (central depot station ID), `t` (maintenance yard station ID), and `d` (total required railcars).
Next `m` lines: `u v cap`, indicating a one-way track from station `u` to station `v` with a limit of `cap` railcars. Stations are numbered 1 to `n`.

## Output
If the relocation is possible, print `YES` on the first line, followed by one line containing `m` integers representing the scheduled number of railcars on each track in the order they were given in the input. If it is not possible, print `NO`. If multiple valid schedules exist, any one is acceptable.

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
