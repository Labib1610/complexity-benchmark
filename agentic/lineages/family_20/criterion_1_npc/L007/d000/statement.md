# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A communications grid consists of junction boxes and fiber links. The network architecture is strictly uniform: exactly three fiber links terminate at every junction box.

During system upgrades, links must be temporarily deactivated. Safety protocols dictate that a junction box will fail if two of its three links are deactivated simultaneously. Therefore, the three links converging at any junction box must be scheduled for deactivation during completely separate time blocks.

The upgrade process is divided into discrete operational phases. Deactivating a link consumes exactly one phase. The physical length of the links and their geographic locations are irrelevant; the only constraint is that links meeting at the same junction box cannot be deactivated in the same phase.

The upgrade must be completed using exactly three operational phases.

Given the layout of the communications grid, you must determine if it is possible to assign every fiber link to one of the three phases such that no junction box is ever compromised. If a valid schedule exists, you must also provide the assignment.

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of junction boxes and fiber links, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating a fiber link connecting junction boxes **u** and **v**.

## Output
If a valid upgrade schedule exists, output `YES` on the first line. On the second line, output **m** integers, each chosen from {1, 2, 3}, representing the phase assigned to each link in the order they appear in the input (links sharing a junction box must be assigned different phases). If no such schedule is possible, output `NO`.

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
