# Problem A — Production Timeline

Time limit: 5 s
Memory limit: 256 MB

## Description
An engineering firm maintains a set of specialized fabrication bays and is currently fulfilling a batch of client orders. Each order consists of a strict progression of fabrication steps. Each step must be performed in a designated bay for a set duration of minutes.

The operational constraints are:
- The steps of a given order must be executed sequentially. A step cannot commence until the prior step of that same order is fully complete.
- A fabrication bay can only accommodate a single step at any given moment.
- Once a step begins in a bay, it must proceed continuously until its required duration is met (no pausing or swapping).

Your task is to schedule all steps to minimize the minute at which every step of every order has been completed. Output this earliest possible completion time.

## Input
The first line contains two integers: the current number of orders and the number of fabrication bays. The firm's logistics limit the maximum number of concurrent orders to the number of pins in a standard ten-pin bowling setup. The building's power grid restricts the maximum number of fabrication bays to the same limit. Both values are at least 1.

Each of the following lines corresponds to one order. It begins with an integer specifying the number of steps in that order, followed by pairs of integers for each step in its required sequence. Each pair specifies the required bay's index (from 1 to the number of bays) and the duration in minutes. Safety regulations mandate that a step's duration is at least 1 and never exceeds the number of millimeters in a standard meter. 

Due to floor space, the aggregate number of steps across all combined orders will not exceed the number of states in the United States of America.

## Output
Print a single integer: the earliest possible minute at which all orders are fully completed.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note
In Example 1, two identical orders each pass through bays 1, 2, and 3 (taking 2 minutes each); the second order trails the first through the sequence and finishes at minute 8. In Example 3, the two orders require different bays and can be executed simultaneously, finishing at minute 4.
