# Problem A — Secure Executive Network

Time limit: 5 s   Memory limit: 256 MB

## Description

A corporation is upgrading the secure intranet in its headquarters. The building contains **n** rooms, each identified by a number from 1 to **n**. You are provided with a list of **m** available bidirectional conduit paths between pairs of rooms, along with the cost to pull secure fiber-optic cable through each path.

There are **t** specific rooms belonging to the board of directors. The board members demand that all of their rooms be mutually able to communicate over the newly installed secure fiber. You may route the connections through any of the other non-board rooms in the building if it reduces the overall installation expense, or you may bypass those extra rooms entirely.

Your task is to select a subset of the available conduit paths to install such that all **t** board rooms are linked together (either directly or via intermediate rooms), minimizing the total installation cost.

## Input

The first line reads three integers **n**, **m**, and **t**. The total number of rooms **n** is bounded by the presence of at least one room and the building's physical capacity of 100 rooms. The count of board rooms **t** requires at least one room and is capped by the 10 available seats on the board of directors. The number of conduits **m** can be as low as 0 and as high as the total number of unique pairs of rooms.

The second line provides **t** distinct integers: the specific room numbers occupied by the board of directors.

Each of the next **m** lines contains three integers **u**, **v**, and **w**. These specify a bidirectional conduit path between room **u** and room **v** (which are distinct valid room numbers from 1 to **n**). The expense **w** to install cable in this conduit is at least 1, and no single cable run will exceed the procurement threshold of 1000000.
It is guaranteed that the available conduits are sufficient to link all board rooms.

## Output

Print a single integer representing the minimum total cost required to link all board rooms.

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

In Example 1, routing the connections through the non-board room 4 (costing 1+1+1 = 3) is cheaper than linking the three board rooms directly (which would cost 4). In Example 3, there is only one board room, so no cabling needs to be installed.
