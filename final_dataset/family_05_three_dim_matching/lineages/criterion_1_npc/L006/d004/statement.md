# Problem A — Grid Installation

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a high-performance computing chassis. The chassis contains a routing grid made of **k** power buses (which form the rows of the grid) and **k** cooling loops (which form the columns). The chassis capacity **k** is between 1 and 22.

A full deployment requires activating exactly **k** grid intersections such that no two activated intersections share the same row, and no two share the same column. 

To operate these intersections, you must install **k** distinct core modules, numbered 1 to **k**. Every activated intersection must receive exactly one core module.

Due to hardware variations, a core module can only operate at specific intersections. You are provided with a database of **t** compatibility records (0 ≤ **t** ≤ **k**·**k**·**k**). Each record specifies that core module **m** is compatible with the intersection at row **c** and column **f**. No record is duplicated.

You must determine if it is possible to select a subset of these compatibility records that forms a full deployment. That is, the chosen subset must collectively utilize every core module exactly once, occupy every row exactly once, and occupy every column exactly once. 

If a valid deployment exists, report one such selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of core modules (which is also the number of rows and columns) and the number of compatibility records. 
Each of the next **t** lines contains three integers **m**, **c**, and **f** (1 ≤ m, c, f ≤ k), representing a compatibility record where module **m** can be placed at row **c** and column **f**. No record is listed more than once.

## Output

If a valid deployment exists, print `YES` on the first line, then print **k** lines, each containing the three integers `m c f` of one chosen record. Any selection meeting all conditions is accepted; the records may be printed in any order.

If no such deployment exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both compatibility records place a module in row 1. Choosing both would violate the condition that every row is occupied exactly once, so it is impossible to form a valid deployment.