# Problem A — Resonance Mitigation in Tethered Artifacts

Time limit: 5 s
Memory limit: 256 MB

## Description
Deep within an ancient security vault, a collection of artifacts remains suspended in mid-air by a web of magical tethers. The vault's architecture distributes the load perfectly: there are exactly one and a half times as many tethers as there are artifacts, and the physical connections are distributed such that every single artifact anchors the exact same number of tethers.

To maintain the suspension safely, you must tune each tether to a specific harmonic frequency. Artifacts are extremely sensitive to interference. If any artifact serves as an anchor for two or more tethers tuned to the identical frequency, the resulting interference will trigger a catastrophic resonance cascade. Consequently, all tethers converging at any given artifact must operate on completely distinct frequencies.

The vault's ancient power source is degraded, strictly limiting the variety of frequencies you can generate. The total number of unique frequencies available for the entire web is exactly equal to the number of tethers anchored to any individual artifact. No additional frequencies can be synthesized.

You are given the layout of the artifacts and tethers. Determine if it is possible to tune every tether without triggering a cascade. If a safe tuning exists, output a valid configuration. Otherwise, you must indicate that the network cannot be stabilized under these constraints.

## Input
The first line contains two integers **n** and **m** (**n** is an even integer, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of artifacts and the number of tethers.
The next **m** lines each contain two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), specifying that a tether spans between artifact **u** and artifact **v**.

## Output
If a safe tuning is possible, print `YES` on the first line. On the second line, print **m** integers corresponding to the frequency assigned to each tether, in the exact order the tethers appear in the input. Frequencies must be represented by positive integers starting from 1 up to the total number of available frequencies. If no safe tuning is possible, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
