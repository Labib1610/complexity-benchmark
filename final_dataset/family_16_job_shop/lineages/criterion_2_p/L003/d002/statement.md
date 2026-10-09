# Problem B — Order Fulfillment

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility is tasked with delivering a batch of **j** custom orders. The fulfillment of each order depends on two unique pieces of equipment: the central mainframe and the testing rig.

The mainframe is responsible for computing the specifications for the orders. It can only process one order at a time. You must choose the sequence in which the mainframe processes the batch. Once started, the mainframe will work continuously through your chosen sequence without any idle time.

Once the mainframe finishes an order, that order immediately becomes available for the testing rig. The testing rig also processes one order at a time. It always selects the available order that finished its mainframe computation earliest. If the mainframe has not yet finished any orders, or if all finished orders have already been processed by the testing rig, the testing rig must wait.

Given the time **p1** required on the mainframe and the time **p2** required on the testing rig for each order, determine the optimal sequence for the mainframe. Your goal is to minimize the total time elapsed from the instant the mainframe starts the first order until the testing rig finishes the last order. Output this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations required for an order on the central mainframe and the testing rig, respectively.

## Output

Print a single integer: the smallest possible total time at which all orders are fully completed.

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

In Example 2, the single order takes 5 on the mainframe and then 3 on the testing rig, finishing at time 8.