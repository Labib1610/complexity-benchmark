# Problem B — Festival Lineup

Time limit: 1 s   Memory limit: 256 MB

## Description

You are organizing a festival featuring **j** distinct performances. Each performance consists of a live act on the Main Stage, followed by a critique session in the Review Room.

Both the Main Stage and the Review Room can only accommodate one performance at a time. The festival follows these scheduling rules:

- You must arrange a schedule for the Main Stage by picking an order for the live acts. The Main Stage hosts them consecutively in this order, starting at time 0, with no idle time between them.
- You must also arrange a schedule for the Review Room by picking an order for the critique sessions. The Review Room can process critiques in a completely different order than the Main Stage if you wish.
- The Review Room processes the critiques one by one in your chosen Review Room sequence. It begins each critique at the earliest possible moment, which is exactly when both of the following conditions are met:
  1. The performance has fully completed its live act on the Main Stage.
  2. The Review Room has finished the critique session of the previous performance in your Review Room sequence (this second condition does not apply to the first critique in the sequence).
- Because the two venues operate independently, the Main Stage can host a later performance while the Review Room is holding a critique for a different one.

You must determine the optimal sequences for both the Main Stage and the Review Room to minimize the total elapsed time. 

What is the earliest possible moment the final critique session in the Review Room can conclude?

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration the performance requires on the Main Stage and in the Review Room, respectively.

## Output

Print a single integer: the minimum possible time at which the Review Room finishes its final critique session.

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

In Example 2, the single performance occupies the Main Stage for 5 time units, and then the Review Room for 3 time units. It finishes at time 8.