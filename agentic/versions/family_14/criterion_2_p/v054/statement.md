# Subterranean Gallery Restoration

Time limit: 2 s   Memory limit: 256 MB

## Description

A team of archaeologists is exploring a vast subterranean structure. The structure is composed of several sealed rooms, which are identified by integers starting from 1 up to **n**. These rooms are connected by a network of blocked passageways. The builders of this structure designed it so that if all passageways were cleared, there would be exactly one unique path between any two rooms. 

The archaeologists have deployed a survey drone whose memory bank can map a positive number of rooms, up to a maximum capacity of two hundred thousand. Because of the builders' strict design, the total number of blocked passageways, **m**, is always exactly one less than the number of rooms **n**.

During the initial scan, the drone identified **t** specific rooms that contain culturally significant frescoes. There is always at least one such room, and depending on the site, it is possible that every single room contains a fresco. The team's goal is to clear a selection of the blocked passageways so that researchers can walk freely between any two rooms containing frescoes without having to leave the cleared portions of the subterranean structure. They may clear passageways that pass through rooms without frescoes if it helps link the fresco rooms together into a single continuous network.

Each blocked passageway requires a specific amount of clearing effort, measured in labor hours. This effort is always a positive integer and, due to the physical limits of debris accumulation, caps out at a maximum of one million labor hours per passageway. The team wants to find the absolute minimum total labor hours necessary to create a fully traversable network connecting all the fresco rooms.

## Input

The first line contains three integers: **n**, **m**, and **t**. The integer **n** is bounded by the drone's positive room capacity described above. The integer **m** is determined by the builders' design, and **t** is bounded by the possible number of fresco rooms.
The second line provides **t** distinct integers representing the identifiers of the rooms that contain frescoes.
The following **m** lines describe the blocked passageways. Each line contains three integers: **u**, **v**, and **w**. The identifiers **u** and **v** indicate the distinct rooms connected by the passageway, while **w** represents the labor hours required to clear it (bounded by the minimum and maximum effort limits described earlier).

## Output

Provide a single integer representing the minimum total labor hours required to ensure all fresco rooms are connected.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
