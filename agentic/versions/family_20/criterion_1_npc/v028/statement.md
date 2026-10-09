# Problem A — Resonance Mitigation in Tethered Artifacts

Time limit: 5 s
Memory limit: 256 MB

## Description
An ancient security vault contains a collection of artifacts, suspended in space by a network of magical tethers. The network is perfectly uniform: if you count the tethers connected to any single artifact, that count is identical for every artifact in the vault. 

To stabilize the vault, every tether must be infused with a specific elemental essence. However, artifacts are highly sensitive to elemental resonance. If any artifact is connected to two or more tethers infused with the identical essence, a catastrophic resonance cascade will occur. Therefore, all tethers meeting at an artifact must carry entirely distinct essences.

You have access to a strictly limited variety of essences. The total number of distinct essences available in the entire vault is exactly equal to the number of tethers attached to any single artifact. There are no additional essences you can use. 

Given the layout of the tethers, determine if it is possible to infuse every tether safely. If it is possible, provide a valid assignment of essences to tethers. If the limited variety of essences makes a safe configuration impossible for this network, you must determine that it cannot be done.

## Input
The first line contains two integers **n** and **m** (**n** is an even integer, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000) representing the number of artifacts and tethers, respectively.
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating that a tether connects artifact **u** and artifact **v**.

## Output
If a safe infusion exists, output `YES` on the first line. On the second line, output **m** integers representing the essence assigned to each tether in the order they were given in the input (tethers sharing an artifact must differ). Use positive integers starting from 1 up to the number of available essences to denote the different essences. If no such infusion is possible, output `NO`.

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
