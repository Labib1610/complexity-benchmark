# Problem A — Acoustic Dampening in Orbital Frames

Time limit: 5 s   Memory limit: 256 MB

## Description
A deep-space habitat is supported by a rigid external frame composed of connection hubs and load-bearing struts. By design, the architecture of the frame is highly uniform: every single hub serves as an endpoint for exactly three struts.

During orbital maneuvers, acoustic vibrations travel through the frame. To mitigate structural fatigue, engineers must manufacture the struts from different alloys. There are exactly three specific alloys available for this purpose, designated as alloy 1, alloy 2, and alloy 3. 

The critical safety requirement dictates the arrangement of these materials at the connections. If any two struts meeting at a hub are made of the same alloy, their identical acoustic properties will create a destructive resonance. Consequently, to maintain structural integrity, the three struts intersecting at any given hub must always be composed of three completely distinct alloys. The physical lengths of the struts and the spatial coordinates of the hubs do not affect this acoustic property; the only factor that matters is ensuring that struts sharing a hub never share an alloy type.

Your task is to process the blueprint of the habitat's frame and assign one of the three available alloys to each strut such that the resonance safety requirement is satisfied everywhere. If the frame's layout makes it impossible to avoid destructive resonance using only the three available alloys, you must report that the blueprint is invalid.

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of connection hubs and the number of load-bearing struts, respectively. Hubs are numbered from 1 to **n**.
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), indicating that a strut connects hub **u** and hub **v**.

## Output
If a safe material assignment is possible, output `YES` on the first line. On the second line, output **m** integers in {1, 2, 3} — the alloy chosen for strut *i* in input order (struts sharing a hub must differ). Otherwise, output `NO`.

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
