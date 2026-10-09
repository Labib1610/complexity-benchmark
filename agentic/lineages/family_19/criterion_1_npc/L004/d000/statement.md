# Problem A — Orbital Logistics Array

Time limit: 5 s
Memory limit: 256 MB

## Description
An orbital station consists of structural junctions connected by one-way transit tubes. Each tube possesses a strict physical tolerance, dictating the absolute maximum number of standard cargo pods it can support during a single operational window. This tolerance applies to the combined total of all pods traversing that specific tube, regardless of who owns them.

Cargo pods are rigid, indivisible units, meaning the number of pods on any given tube is always a non-negative whole number. As pods move through the station, they must be strictly conserved. For any given syndicate, at any junction that is neither their starting point nor their final terminus, the exact number of their pods arriving at the junction must equal the number of their pods departing from it. Pods cannot be stored at intermediate junctions.

During the upcoming operational window, several distinct syndicates need to transfer their assets. Each syndicate has a designated injection junction where their pods enter the network, a designated extraction junction where their pods must arrive, and a strict integer quota of pods they need to move. At an injection junction, the net outflow of a syndicate's pods exactly equals their quota; at an extraction junction, the net inflow exactly equals their quota. The syndicates operate independently but rely on the identical shared tube infrastructure. Transit times, physical distances, and tube lengths are irrelevant to this planning phase; only the structural tolerances, pod conservation, and syndicate quotas matter.

Your task is to produce a routing configuration that successfully delivers every syndicate's full quota simultaneously without exceeding the physical tolerance of any transit tube, or to determine that the network cannot support all syndicates at once. (While routing a single syndicate's pods might be straightforward, the challenge arises from all syndicates simultaneously competing for the shared tube tolerances.)

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of structural junctions, transit tubes, and syndicates, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the injection junction, extraction junction, and exact pod quota for syndicate $i$.
The following $m$ lines each contain three integers $u$, $v$, and $cap$, detailing a one-way transit tube from junction $u$ to junction $v$ with a physical tolerance of $cap$ pods.

## Output
If a valid configuration exists, output `YES` on the first line. Following this, output $k$ lines. The $i$-th line must contain $m$ integers representing the exact number of pods syndicate $i$ routes through each of the $m$ tubes, given in the same order the tubes appeared in the input. If no such configuration is possible, output `NO`.

## Example

### Input
```
4 5 2
1 4 1
2 3 1
1 2 1
2 3 1
3 4 1
1 3 1
2 4 1
```

### Output
```
YES
1 0 0 0 1
0 1 0 0 0
```
