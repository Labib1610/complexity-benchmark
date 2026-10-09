# Problem A — Tri-Port Network Frequency Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description
A deterministic communication fabric is built entirely from identical switching modules. The architecture is completely uniform: every single module is equipped with exactly three bidirectional links connecting it to other modules. There are no edge cases, no varying capacities, and no missing connections; the link count of every module is rigidly fixed at three.

The fabric operates using three distinct communication frequencies, labeled 1, 2, and 3. To guarantee zero signal interference at the hardware level, every module must have its three connected links configured to use all three different frequencies. Consequently, at any given module, exactly one link operates on frequency 1, exactly one on frequency 2, and exactly one on frequency 3.

Because the local structure is perfectly balanced and highly constrained—each module requires exactly one of each frequency—configuring a single link immediately restricts the available options for neighboring links. In many practical deployments, this rigid local symmetry allows a configuration to cascade smoothly across the entire fabric without conflict, as each choice heavily limits the remaining search space. However, depending on how the links form global loops, a fully consistent configuration might still be impossible.

Your task is to determine whether it is possible to assign a frequency to every link such that the strict local interference rules are satisfied everywhere. If a valid configuration exists, you must provide one.

## Input
The first line contains two integers **n** and **m** (where **n** is an even integer, **m** = 3**n**/2, and 2 ≤ **n** ≤ 2000), representing the number of switching modules and the total number of bidirectional links, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating a bidirectional link between module **u** and module **v**. It is guaranteed that every module appears in exactly three links.

## Output
If a valid frequency assignment exists, print `YES` on the first line. On the second line, print **m** integers chosen from {1, 2, 3}, representing the frequency assigned to each link in the exact order they were given in the input. If multiple valid assignments exist, you may output any of them.
Otherwise, print `NO`.

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
