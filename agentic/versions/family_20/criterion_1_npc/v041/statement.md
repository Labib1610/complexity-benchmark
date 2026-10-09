# Problem A — Fluid Distribution Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical plant operates a fluid distribution network consisting of mixing vats and connecting pipes. The network has been engineered so that exactly three pipes meet at each vat. 

Each pipe must be configured to operate at a specific pressure level, chosen from the values 1, 2, or 3. 

To maintain equilibrium, the pressure levels must be balanced. Specifically, for every mixing vat in the network, the product of the pressure levels of the three pipes connected to it must be exactly 6. The physical lengths of the pipes and the materials used are irrelevant to the configuration—the only requirement is that this pressure product condition is satisfied at every vat.

Determine if it is possible to assign a pressure level of 1, 2, or 3 to each pipe such that the equilibrium condition holds everywhere. If it is possible, provide one such valid assignment.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of vats and pipes, respectively.
Each of the next **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a pipe connecting vat u and vat v. 

## Output
If a valid configuration exists, print `YES`, followed by a line with **m** integers in {1, 2, 3} — the pressure level of pipe i in the order they were given in the input. Otherwise, print `NO`.

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
