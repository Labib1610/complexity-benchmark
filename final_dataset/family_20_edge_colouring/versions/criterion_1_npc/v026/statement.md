# Problem A — Polymer Pipeline: Phase Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
You are implementing the middle stage of an automated machine-learning pipeline for designing synthetic polymers. The pipeline operates in three consecutive stages:

**Stage 1: Topology Generation (Pre-processing)**
An upstream module constructs a candidate scaffold consisting of atoms and connecting bonds. The generator is strictly constrained by valency rules to only produce scaffolds where every single atom participates in exactly three bonds.

**Stage 2: Phase Assignment (Your Task)**
You must configure each bond with one of three distinct resonance phases (labeled 1, 2, and 3). 
For the downstream simulation to converge safely, the local environment around every atom must be perfectly balanced. This means no two bonds connected to the same atom can share the same phase. Because every atom has exactly three bonds and there are only three phases available, every atom must be connected to exactly one bond of phase 1, one of phase 2, and one of phase 3.

**Stage 3: Simulation (Post-processing)**
A quantum chemistry solver takes the phase-assigned scaffold to simulate electron densities. If you can find a valid phase configuration for all bonds, you must output it so it can be passed to this solver. If no such configuration exists, you must reject the scaffold so the pipeline can discard it and request a new topology from Stage 1.

## Input
The first line contains two integers **n** and **m** (where **n** is even, **m** = 3**n**/2, and 2 ≤ **n** ≤ 2000), representing the number of atoms and the total number of bonds produced by Stage 1.
Each of the next **m** lines contains two integers *u* and *v* (1 ≤ *u* < *v* ≤ **n**), indicating a bond between atom *u* and atom *v*.

## Output
If a valid phase assignment exists for Stage 3, output `YES` on the first line. On the second line, output **m** integers from the set {1, 2, 3}, representing the phase assigned to each bond in the exact order they were given in the input. If multiple valid configurations exist, you may output any of them.
If no valid assignment is possible, output `NO`.

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
