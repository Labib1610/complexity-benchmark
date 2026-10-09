# Tunable Wavelengths in Optical Circuits

Time limit: 5 s   Memory limit: 256 MB

## Description
An experimental quantum network is built from a set of optical nodes connected by bidirectional fiber segments. The topology is strictly uniform: every single node in the network is an endpoint for exactly three fiber segments.

To transmit data without destructive interference, each fiber segment must be calibrated to carry light at one of three available frequencies. The hardware at each node is designed to merge and route signals, but it has a strict physical limitation: a node will only function correctly if the three segments connected to it are all carrying different frequencies. If any two segments meeting at the same node share a frequency, the resulting resonance will destroy the quantum state. 

There are exactly three frequencies available, represented by the integers 1, 2, and 3. Given the layout of the network, determine whether it is possible to assign every fiber segment one of these three frequencies so that the interference constraint is satisfied everywhere. 

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of optical nodes and fiber segments, respectively. Nodes are numbered 1 to **n**.
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating a fiber segment connecting node **u** and node **v**.

## Output
If a valid calibration exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} — the frequency assigned to each fiber segment in the order they were given in the input (segments sharing a node must differ). If no such calibration is possible, print `NO`.

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
