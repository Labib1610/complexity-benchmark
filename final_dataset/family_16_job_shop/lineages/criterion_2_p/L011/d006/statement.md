# Problem B — Batch Processing Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

You are orchestrating a sequence of **j** operations. Each operation consists of a Prepare task followed by a Finalize task. 

You must establish a single processing sequence (an ordering of the **j** operations). Both the Prepare tasks and the Finalize tasks will be executed in this exact same order.

The execution timeline is determined by the following rules:
1. A single Prepare worker executes the Prepare tasks continuously, one after another in your chosen sequence, starting at time 0. 
2. A single Finalize worker executes the Finalize tasks one after another in the exact same sequence.
3. For any given operation, the Finalize worker cannot begin its Finalize task until two conditions are met:
   - The Prepare worker has completely finished that operation's Prepare task.
   - The Finalize worker has completely finished the previous operation's Finalize task (this applies to all operations after the first).
4. The Finalize worker begins each task at the earliest possible time that satisfies the conditions above.

Your task is to find an ordering of the **j** operations that minimizes the total time required—specifically, the time when the Finalize worker completes the final operation in your sequence.

What is the minimum possible completion time?

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the time required for the operation's Prepare task and Finalize task, respectively.

## Output

Print a single integer: the minimum possible completion time of the last Finalize task.

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

In Example 1, if we order the operations as the 3rd operation, then the 2nd operation, then the 1st operation from the input:
- The 3rd operation takes 1 for its Prepare task (finishes at time 1). Its Finalize task takes 3, starting at 1 and finishing at 4.
- The 2nd operation takes 2 for its Prepare task (finishes at 1+2=3). Its Finalize task takes 4. It must wait for its Prepare task (time 3) and the previous Finalize task (time 4). It starts at 4 and finishes at 4+4=8.
- The 1st operation takes 3 for its Prepare task (finishes at 3+3=6). Its Finalize task takes 2. It must wait for its Prepare task (time 6) and the previous Finalize task (time 8). It starts at 8 and finishes at 8+2=10.
The final completion time is 10. This is the minimum possible time across all valid orderings.

In Example 2, there is only one operation. The Prepare worker finishes at 5. The Finalize worker starts at 5 and finishes at 5 + 3 = 8.