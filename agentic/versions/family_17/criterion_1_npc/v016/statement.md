# Problem A — Complete Roster Squad Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The orbital command center is preparing a full-scale asteroid extraction drill. Every active mining drone on the roster must be committed to the exercise. The roster is fixed for the duration of the drill and consists of a pool of drones, each assigned a unique serial number running consecutively from 1 to 3q.

Drones are only ever fielded in **squads of exactly three**. Due to complex harmonic resonance in their cutting lasers, command can only field a squad if that precise three-drone triplet appears on the pre-calibrated list; ad-hoc triplets are strictly forbidden. The pre-calibrated list has been assembled from historical testing, so a single drone may well appear in many different calibrated triplets, and some triplets may overlap heavily.

A deployment plan is an activation of some subset of the calibrated triplets. The plan is authorized only when it satisfies all of the following strict operational constraints:
1. The activated triplets must tile the whole roster perfectly: **every** drone from 1 to 3q must appear in **exactly one** activated squad (no drone omitted, no drone shared).
2. The deployment must activate exactly q squads.
3. The grand total of the serial numbers of all drones in the activated squads must equal exactly 3q(3q+1)/2.
4. No individual activated squad may have a serial number sum exceeding 9q - 3.

Your task is to decide whether the calibrated triplets admit an authorized deployment plan, and if they do, to produce one such plan. If the calibrated list cannot account for the entire roster under these rules, report that no authorized plan exists.

## Input
The first line contains two integers q and t (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next t lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), representing a calibrated triplet.

## Output
If a valid deployment plan exists, print `YES` on the first line, followed by q lines each containing the three serial numbers of one chosen triplet.
Otherwise, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
