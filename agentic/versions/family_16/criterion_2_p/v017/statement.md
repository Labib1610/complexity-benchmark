# Problem B — Supply Chain Synchronization

Time limit: 1 s   Memory limit: 256 MB

## Description

A global manufacturing operation is divided into three distinct phases: Procurement, Assembly, and Freight. 

The Procurement phase has just concluded, depositing the raw materials for **j** separate orders into the staging area of your facility. Your focus is strictly on the Assembly phase.

During Assembly, every order must be routed through two specialized stations in strict succession: the Molder and the Welder. The operational rules for this phase are as follows:
- The Molder and the Welder can each handle only one order at any given time.
- An order can only commence at the Welder after it has fully completed its duration at the Molder.
- The factory's automated track requires that the sequence of orders fed into the Molder is identical to the sequence of orders fed into the Welder. You are free to choose this sequence.

Once the Assembly phase is entirely concluded, the Freight phase is triggered. A fleet of autonomous trucks will dispatch the goods to global distributors. However, the fleet is programmed to depart only when the very last order has finished processing at the Welder.

Determine the optimal order sequence to minimize the total duration of the Assembly phase, and report the earliest time at which the Freight phase can initiate.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), representing the number of orders provided by the Procurement phase.
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing durations of an order at the Molder and at the Welder, respectively.

## Output

Print a single integer: the earliest possible time at which all orders are completed and the Freight phase can initiate.

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

In Example 2, the single order takes 5 time units on the Molder then 3 time units on the Welder, finishing at time 8.
