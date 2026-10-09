# Problem B — Spaceport Clearance

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing the arrival of **j** starships. Each starship requires an atmospheric entry duration (**p1**) followed by a surface landing duration (**p2**).

You must arrange all **j** starships into a single arrival sequence. Let the chosen sequence of starships be placed into positions $1, 2, \dots, j$, where $p1_i$ and $p2_i$ are the durations for the starship assigned to position $i$.

The timeline of operations is determined as follows:
- The atmospheric entry corridor can only accommodate one starship at a time. Starship $i$ begins its entry immediately after starship $i-1$ completes its entry. The first starship begins at time 0.
- The surface landing pad can also only accommodate one starship at a time. Starship $i$ begins its landing process as soon as both of the following conditions are met: it has fully completed its own atmospheric entry, and starship $i-1$ has fully completed its landing. (The first starship begins landing as soon as its entry is complete).

The overall clearance time of your sequence is the exact moment the $j$-th starship finishes its landing process. 

Find an ordering of the starships that makes their overall clearance time as small as possible, and report this smallest possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the atmospheric entry duration and the landing duration of a starship.

## Output

Print a single integer: the smallest possible overall clearance time.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, an optimal arrangement places the starships in the order of the 3rd, 2nd, and 1st from the input.
- The 3rd input starship (durations 1 and 3) enters from time 0 to 1, and lands from 1 to 4.
- The 2nd input starship (durations 2 and 4) enters from time 1 to 3, and lands from 4 to 8.
- The 1st input starship (durations 3 and 2) enters from time 3 to 6, and lands from 8 to 10.
The clearance time is 10.