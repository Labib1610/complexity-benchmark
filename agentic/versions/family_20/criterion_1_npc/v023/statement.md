# Problem A — Atmospheric Cycle Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description
A deep-space habitat consists of a network of habitation pods connected by transfer tubes. The habitat's life-support core has a strict capacity limit, capable of sustaining a maximum of 2000 pods. A minimal functional habitat consists of exactly 2 pods. Due to structural symmetry, the total number of pods is always an even number. 

Every pod is built with exactly three airlocks, and every airlock is sealed to a transfer tube leading to another pod. This means every pod serves as a junction for exactly three tubes. Consequently, the total number of tubes in the habitat is always exactly one and a half times the number of pods.

To prevent material fatigue, each transfer tube must be assigned to one of three atmospheric pressurization cycles (labeled 1, 2, and 3). If any two tubes connected to the same pod are assigned the same pressurization cycle, the unbalanced pressure will cause the pod's structural integrity to fail. Therefore, at any single pod, the three connected tubes must be assigned to three completely different cycles.

Given the layout of the habitat, you must assign each tube one of the three cycles so that the habitat remains safe, or determine that no such safe assignment exists.

## Input
The first line contains two integers **P** and **T**, representing the number of pods and the number of transfer tubes, respectively. The bounds on $P$ and the exact relationship between $P$ and $T$ are determined by the habitat's physical limits described above.

Each of the next **T** lines describes a transfer tube by specifying the two pods it connects. Pods are identified by sequential integers starting from 1 up to the total number of pods. For each tube, the two pod identifiers are given separated by a space, with the smaller identifier always listed first.

## Output
If a safe assignment exists, print `YES`, followed by a line containing **T** integers from the set {1, 2, 3}. The $i$-th integer must represent the pressurization cycle assigned to the $i$-th tube in the input order. If there are multiple valid assignments, any one will be accepted.
If no such assignment is possible for the given habitat, print `NO`.

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
