# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a manufacturing process with $j$ custom orders. Each order requires fabrication on Machine 1, and only after that is fully completed, finishing on Machine 2. A machine can process at most one order at any given moment.

The factory has a strict operating shift of $T$ minutes. All orders must complete both fabrication and finishing within this shift.

For every input, it is guaranteed that the shift is too short to fulfill all orders, no matter how they are scheduled. Furthermore, exactly one of the following two proofs of impossibility will apply. Your task is to verify the orders and output the code for the proof that applies:

- `JOB i` (where $i$ is the 1-based index of an order): The shift duration is strictly less than the time needed to put this single order through Machine 1 and then Machine 2 sequentially. Thus, it cannot be completed in time even if it were the only order in the factory.
- `LOAD c` (where $c$ is 1 or 2): The shift duration is strictly less than the aggregate time Machine $c$ must run to process its part of all $j$ orders. Thus, the machine's workload exceeds the shift even if we completely ignore the dependency between fabrication and finishing.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in minutes for the order's fabrication on Machine 1 and its finishing on Machine 2, respectively.

## Output

Print a single line containing either `JOB i` (if order $i$'s sequential duration alone exceeds the shift) or `LOAD c` (if Machine $c$'s total workload alone exceeds the shift).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, the first order requires 70 minutes on Machine 1 and then 60 minutes on Machine 2 sequentially. It cannot complete its own sequence within the 100-minute shift, making `JOB 1` a valid proof of impossibility. 

In Example 2, no individual order's sequence violates the 150-minute shift. However, Machine 1 is assigned four fabrication tasks of 50 minutes each. Since a machine operates on only one task at a time, it cannot complete its assigned workload within the shift, making `LOAD 1` the valid proof.