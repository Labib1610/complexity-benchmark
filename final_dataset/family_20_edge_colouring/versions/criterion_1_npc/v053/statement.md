# Balanced Load Distribution in Uniform Grids

Time limit: 5 s   Memory limit: 256 MB

## Description
A communications grid relies on a network of junction boxes and fiber links. The network architecture is strictly uniform by design: exactly three fiber links terminate at every single junction box.

The network requires periodic maintenance, which involves temporarily deactivating the fiber links. The maintenance process is organized into exactly three discrete operational phases. Deactivating a link takes exactly one full phase. Network safety protocols dictate that a junction box will fail if two of its terminating links are deactivated during the same phase.

Because the number of available operational phases perfectly matches the number of links per junction box, any valid schedule will be perfectly balanced locally and globally. For the grid to remain stable, every individual junction box must have exactly one of its links deactivated in phase 1, exactly one in phase 2, and exactly one in phase 3. This strict uniformity means the total number of link deactivations is exactly the same across all three phases network-wide.

Given the layout of the grid's connections, determine if such a perfectly balanced maintenance schedule exists. If it is possible to assign every fiber link to one of the three phases to maintain stability across all junction boxes, you must provide the assignment.

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of junction boxes and fiber links, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating a fiber link connecting junction boxes **u** and **v**.

## Output
If a valid maintenance schedule exists, output `YES` on the first line. On the second line, output **m** integers, each chosen from {1, 2, 3}, representing the phase assigned to each link in the order they appear in the input (links sharing a junction box must be assigned different phases). If no such schedule is possible, output `NO`.

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
