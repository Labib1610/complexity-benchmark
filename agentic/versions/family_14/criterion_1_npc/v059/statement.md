# Subterranean Reunion

Time limit: 5 s   Memory limit: 256 MB

## Description

A subterranean expedition has discovered a complex of **n** caverns, numbered 1 to **n**. Between certain pairs of caverns, there are collapsed ancient passages. Excavating a passage requires a specific amount of effort.

The expedition members are currently stranded in **t** specific caverns. They must reunite by excavating a selection of the collapsed passages. The chosen passages must allow a person to travel from any of the **t** stranded caverns to any other of the **t** stranded caverns, using only the excavated passages. The expedition is free to excavate passages that lead through any of the remaining **n** - **t** empty caverns if doing so reduces the total effort, or they can avoid them entirely.

Determine the lowest possible total excavation effort required to reunite the expedition members.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of caverns, the number of collapsed passages, and the number of caverns containing stranded members, respectively.

The second line contains **t** distinct integers: the numerical IDs of the caverns where members are stranded.

Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a two-way passage between cavern **u** and cavern **v** can be excavated with an effort of **w**.

It is guaranteed that the available passages are sufficient to reunite all members.

## Output

Print a single integer: the minimum total effort to excavate the necessary passages.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, excavating passages through the empty cavern 4 requires 1 + 1 + 1 = 3 effort. This is less effort than excavating passages to connect the three stranded caverns directly to each other, which would require an effort of at least 4. In Example 3, there is only one cavern with stranded members, so they are already united and no passages need to be excavated.
