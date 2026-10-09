# Problem B — Certification Workflow

Time limit: 2 s
Memory limit: 256 MB

## Description

The annual factory certification process is divided into three consecutive phases:

1. **Hardware Allocation:** The HR department assigns each of the $k$ operators (numbered 1 to $k$) to a unique control terminal (numbered 1 to $k$). This ensures every operator has an exclusive terminal.
2. **Scheduling:** The logistics system assigns each operator-terminal pair to one of $k$ distinct testing windows (numbered 1 to $k$).
3. **Execution and Logging:** The automated system runs the tests and analyzes the generated logs.

Your task is to implement the software for the **Scheduling** phase.

Due to maintenance constraints, an operator at their specific terminal can only be scheduled during certain testing windows. You will receive a list of approved configurations, each specifying an operator, a terminal, and a testing window. Because the Hardware Allocation phase has already concluded, you will notice that in the provided list, each operator is associated with exactly one terminal, and no terminal is assigned to more than one operator.

Your goal is to choose exactly $k$ configurations from the approved list so that the schedule is complete: every operator is tested, every terminal is used, and every testing window is occupied exactly once. If this is possible, output the finalized schedule so the Execution phase can begin.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of operators (which is also the number of terminals and windows) and the number of approved configurations.

The following $t$ lines each contain three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$) representing an approved configuration consisting of operator $x$, terminal $y$, and testing window $z$. No configuration is repeated. As guaranteed by the first phase of the workflow, any configurations involving the same operator $x$ will always feature the same terminal $y$, and different operators will be paired with different terminals.

## Output

If a complete schedule exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of a selected configuration. These configurations can be printed in any order. Any valid complete schedule will be accepted.

If no such schedule is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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
