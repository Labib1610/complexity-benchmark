# Problem B — Adversarial Grid Path

Time limit: 1 s   Memory limit: 256 MB

## Description

You are given a set of **j** tiles. Each tile is a vertical column consisting of two cells: a top cell with value **p1**, and a bottom cell with value **p2**.

You must arrange all **j** tiles side by side in a sequence of your choosing to form a grid with 2 rows and **j** columns. The top cells form the first row, and the bottom cells form the second row.

An adversary will start at the top-left cell of your grid (row 1, column 1) and travel to the bottom-right cell (row 2, column **j**). In each step, the adversary can either move one cell to the right or one cell down. Moving left or up is not allowed. 

The cost of a path is defined as the sum of the values in all cells visited along the path, including the starting and ending cells. The adversary is guaranteed to choose a valid path that maximizes this total cost.

Your task is to find a left-to-right arrangement of the **j** tiles that minimizes the maximum path cost the adversary can achieve. Output this minimum possible maximum cost.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the value of the top cell and the value of the bottom cell of a tile, respectively.

## Output

Print a single integer: the smallest possible maximum path cost the adversary can achieve, given your optimal arrangement of the tiles.

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

In Example 1, one optimal arrangement is to place the 3rd tile first, then the 2nd tile, and finally the 1st tile.
The grid becomes:
Row 1: 1, 2, 3
Row 2: 3, 4, 2

The adversary can choose from three possible paths:
- Move down at column 1: The visited cells are (1,1) -> (2,1) -> (2,2) -> (2,3). The cost is 1 + 3 + 4 + 2 = 10.
- Move down at column 2: The visited cells are (1,1) -> (1,2) -> (2,2) -> (2,3). The cost is 1 + 2 + 4 + 2 = 9.
- Move down at column 3: The visited cells are (1,1) -> (1,2) -> (1,3) -> (2,3). The cost is 1 + 2 + 3 + 2 = 8.

The adversary will choose the first path to maximize the cost, resulting in a cost of 10. No other arrangement of the tiles can force the adversary's maximum cost to be strictly less than 10.

In Example 2, there is only 1 tile. The only path visits the top cell (5) and then the bottom cell (3). The cost is 5 + 3 = 8.