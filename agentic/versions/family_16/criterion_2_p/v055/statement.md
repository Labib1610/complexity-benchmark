# Problem B — Automated Bakery Line

Time limit: 1 s   Memory limit: 256 MB

## Description

A commercial bakery is processing a batch of custom cakes through a two-stage automated production line. The line consists of a convection oven and a subsequent robotic frosting applicator. 

The oven accommodates only one cake at a time, and the frosting applicator accommodates only one cake at a time. A cake can only advance to the frosting applicator after its full duration in the oven is complete. Cakes may wait in a queue between the two machines if necessary, but they must be processed by the frosting applicator in the exact same sequence they were fed into the oven.

You are given the required oven duration and applicator duration for each cake. You must choose the initial feeding sequence to minimize the total elapsed time from when the first cake enters the oven until the final cake completes its frosting stage.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), representing the number of cakes.
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the oven duration and the frosting duration for a cake, respectively.

## Output

Print a single integer representing the minimum possible total elapsed time to finish all cakes.

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

In Example 2, the single cake requires 5 units of time in the oven and 3 units in the applicator, completing at time 8.
