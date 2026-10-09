# Problem B — Interference-Free Monitoring

Time limit: 2 s   Memory limit: 256 MB

## Description

An intricate clockwork mechanism consists of **n** gears (numbered 1 to **n**) and **m** meshing points. Each meshing point engages two specific gears together. 

The manufacturer guarantees that the gear network is physically workable: the entire system can rotate freely without jamming. Because they mesh, any two connected gears must turn in opposite directions, meaning the network's gears can be consistently assigned a valid rotation direction (clockwise or counter-clockwise) without any contradictions. (You are not given the rotation directions; you may deduce them from the meshing points if needed).

You have been tasked with installing diagnostic sensors on exactly **k** of these gears. Because the sensors emit strong magnetic fields, they will interfere with each other if placed on gears that physically touch. Therefore, no two gears chosen for sensor installation can mesh with each other.

Given the target size **k**, decide whether it is possible to select exactly **k** gears for sensor installation without any interference, and if so, report a valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that gear **u** and gear **v** mesh together. No meshing pair is listed twice, and the arrangement is guaranteed to be workable as described above.

## Output

If a valid set of **k** gears can be monitored, print `YES` on the first line, then on the second line print **k** distinct gear numbers forming such a set, separated by spaces. Any valid set where no two selected gears mesh is accepted.

If no such set exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```
